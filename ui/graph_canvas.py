import tkinter as tk
import math
import random


class GraphCanvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(
            master,
            bg="#ffffff",
            highlightthickness=0,
            scrollregion=(0, 0, 3000, 3000)
        )

        self.graph = None
        self.positions = {}
        self.tooltip = None
        self.scale_factor = 1.0

        # Pan & Zoom
        self.bind("<ButtonPress-1>", self.start_pan)
        self.bind("<B1-Motion>", self.do_pan)
        self.bind("<MouseWheel>", self.zoom)

    # ======================================================
    # FORCE DIRECTED LAYOUT (ÜST ÜSTE BİNME YOK)
    # ======================================================
    def compute_force_layout(self, graph, iterations=60):
        nodes = list(graph.nodes.keys())
        n = len(nodes)

        width = max(self.winfo_width(), 1200)
        height = max(self.winfo_height(), 800)

        k = math.sqrt((width * height) / max(n, 1))
        MIN_DIST = 40  # düğümler arası minimum mesafe

        # Rastgele başlangıç
        pos = {
            node: (
                random.uniform(200, width - 200),
                random.uniform(200, height - 200)
            )
            for node in nodes
        }

        for _ in range(iterations):
            disp = {node: [0.0, 0.0] for node in nodes}

            # Repulsion
            for i in range(n):
                for j in range(i + 1, n):
                    dx = pos[nodes[i]][0] - pos[nodes[j]][0]
                    dy = pos[nodes[i]][1] - pos[nodes[j]][1]
                    dist = math.hypot(dx, dy) + 0.01

                    if dist < MIN_DIST:
                        force = (k * k) / dist * 3
                    else:
                        force = (k * k) / dist

                    disp[nodes[i]][0] += (dx / dist) * force
                    disp[nodes[i]][1] += (dy / dist) * force
                    disp[nodes[j]][0] -= (dx / dist) * force
                    disp[nodes[j]][1] -= (dy / dist) * force

            # Attraction
            for node_id, node in graph.nodes.items():
                for neighbor in node.neighbors:
                    dx = pos[node_id][0] - pos[neighbor][0]
                    dy = pos[node_id][1] - pos[neighbor][1]
                    dist = math.hypot(dx, dy) + 0.01
                    force = (dist * dist) / k

                    disp[node_id][0] -= (dx / dist) * force
                    disp[node_id][1] -= (dy / dist) * force

            # Güncelle
            for node in nodes:
                x = pos[node][0] + disp[node][0] * 0.01
                y = pos[node][1] + disp[node][1] * 0.01

                x = min(width - 100, max(100, x))
                y = min(height - 100, max(100, y))
                pos[node] = (x, y)

        return pos

    # ======================================================
    # GRAPH ÇİZİMİ
    # ======================================================
    def draw_graph(self, graph, colors=None, highlight_path=None):
        self.graph = graph
        self.delete("all")

        if not graph or not graph.nodes:
            return

        self.positions = self.compute_force_layout(graph)

        # ------------------ EDGES ------------------
        for node_id, node in graph.nodes.items():
            for neighbor in node.neighbors:
                if node_id < neighbor:
                    x1, y1 = self.positions[node_id]
                    x2, y2 = self.positions[neighbor]

                    is_path = False
                    if highlight_path:
                        for i in range(len(highlight_path) - 1):
                            if (
                                highlight_path[i] == node_id
                                and highlight_path[i + 1] == neighbor
                            ) or (
                                highlight_path[i] == neighbor
                                and highlight_path[i + 1] == node_id
                            ):
                                is_path = True
                                break

                    color = "#3498db" if is_path else "#d1d8e0"
                    width_line = 4 if is_path else 1

                    line = self.create_line(
                        x1, y1, x2, y2,
                        fill=color,
                        width=width_line,
                        smooth=True
                    )
                    self.tag_bind(
                        line,
                        "<Enter>",
                        lambda e, n1=node_id, n2=neighbor: self.show_edge_info(e, n1, n2)
                    )
                    self.tag_bind(line, "<Leave>", self.hide_tooltip)

        # ------------------ NODES ------------------
        palette = {
            1: "#e74c3c",
            2: "#2ecc71",
            3: "#3498db",
            4: "#f1c40f",
            5: "#9b59b6"
        }

        for node_id, (x, y) in self.positions.items():
            fill = "#ecf0f1"

            if highlight_path and node_id in highlight_path:
                fill = "#3498db"
            elif colors:
                fill = palette.get(colors[node_id], "#95a5a6")

            self.create_oval(
                x - 18, y - 18, x + 18, y + 18,
                fill="#ffffff", outline="#dcdde1", width=2
            )

            node_circle = self.create_oval(
                x - 15, y - 15, x + 15, y + 15,
                fill=fill, outline="#2f3542", width=1
            )

            self.create_text(
                x, y, text=str(node_id),
                fill="#2f3542", font=("Arial", 9, "bold")
            )

            self.tag_bind(
                node_circle,
                "<Enter>",
                lambda e, nid=node_id: self.show_node_info(e, nid)
            )
            self.tag_bind(node_circle, "<Leave>", self.hide_tooltip)

        self.configure(scrollregion=self.bbox("all"))

    # ======================================================
    # TOOLTIP
    # ======================================================
    def show_node_info(self, event, node_id):
        node = self.graph.nodes[node_id]
        text = f"Düğüm: {node.id}\nİsim: {node.name}\nDerece: {len(node.neighbors)}"
        self.create_tooltip_box(event.x_root, event.y_root, text)

    def show_edge_info(self, event, n1, n2):
        from src.utils import get_dynamic_weight
        node_i = self.graph.nodes[n1]
        node_j = self.graph.nodes[n2]
        weight = get_dynamic_weight(node_i, node_j)

        text = (
            f"{node_i.name} ↔ {node_j.name}\n"
            f"Maliyet: {weight:.4f}"
        )
        self.create_tooltip_box(event.x_root, event.y_root, text)

    def create_tooltip_box(self, x, y, text):
        self.hide_tooltip()
        self.tooltip = tk.Toplevel(self)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x + 15}+{y + 10}")

        label = tk.Label(
            self.tooltip, text=text,
            justify="left",
            background="#2f3542",
            foreground="white",
            padx=8, pady=4,
            font=("Arial", 9)
        )
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    # ======================================================
    # PAN & ZOOM
    # ======================================================
    def start_pan(self, event):
        self.scan_mark(event.x, event.y)

    def do_pan(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

    def zoom(self, event):
        factor = 1.1 if event.delta > 0 else 0.9
        self.scale_factor *= factor
        self.scale("all", event.x, event.y, factor, factor)
        self.configure(scrollregion=self.bbox("all"))
