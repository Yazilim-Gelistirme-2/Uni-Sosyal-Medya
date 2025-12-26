import tkinter as tk
import math

class GraphCanvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, bg="white", highlightthickness=0)
        self.positions = {}
        self.color_palette = ["#1f6feb", "#28a745", "#e74c3c", "#f1c40f", "#9b59b6", "#e67e22", "#1abc9c"]
        self.bind("<Motion>", self.on_mouse_move)

    def draw_graph(self, graph, colors=None, highlight_path=None):
        self.graph = graph 
        self.delete("all")
        if not graph or not graph.nodes: return

        # 1. Pozisyon Hesaplama
        nodes = list(graph.nodes.keys())
        w = self.winfo_width() if self.winfo_width() > 1 else 600
        h = self.winfo_height() if self.winfo_height() > 1 else 600
        cx, cy = w/2, h/2
        r = min(cx, cy) * 0.7
        
        for i, nid in enumerate(nodes):
            angle = 2 * math.pi * i / len(nodes)
            self.positions[nid] = (cx + r * math.cos(angle), cy + r * math.sin(angle))

        # 2. Kenarları (Yolları) Çiz
        path_edges = set()
        if highlight_path and len(highlight_path) > 1:
            for i in range(len(highlight_path) - 1):
                u, v = highlight_path[i], highlight_path[i+1]
                path_edges.add(tuple(sorted((u, v))))

        for nid, node in graph.nodes.items():
            x1, y1 = self.positions[nid]
            for neighbor in node.neighbors:
                if neighbor in self.positions and nid < neighbor:
                    x2, y2 = self.positions[neighbor]
                    is_path = tuple(sorted((nid, neighbor))) in path_edges
                    l_color = "#1f6feb" if is_path else "#d1d5da"
                    l_width = 4 if is_path else 2 
                    tag = f"edge_{nid}_{neighbor}"
                    self.create_line(x1, y1, x2, y2, fill=l_color, width=l_width, tags=(tag, "edge"))

        # 3. Düğümleri Çiz
        for nid, (x, y) in self.positions.items():
            if colors and nid in colors:
                base_color = self.color_palette[colors[nid] % len(self.color_palette)]
            elif highlight_path and nid in highlight_path:
                base_color = "#28a745"
            else:
                base_color = "#1f6feb"

            tag = f"node_{nid}"
            self.create_oval(x-14, y-14, x+14, y+14, fill="white", outline=base_color, width=2, tags=(tag, "node"))
            self.create_text(x, y, text=str(nid), fill="black", font=("Arial", 9, "bold"), tags=(tag, "node"))

    def on_mouse_move(self, event):
        self.hide_tooltip()
        item = self.find_closest(event.x, event.y)
        tags = self.gettags(item)
        
        for tag in tags:
            if tag.startswith("node_"):
                nid = int(tag.split("_")[1])
                nx, ny = self.positions[nid]
                if math.sqrt((event.x - nx)**2 + (event.y - ny)**2) <= 15:
                    self.show_node_tooltip(event.x, event.y, nid)
                    return 

        overlapping = self.find_overlapping(event.x-2, event.y-2, event.x+2, event.y+2)
        for item in overlapping:
            tags = self.gettags(item)
            for tag in tags:
                if tag.startswith("edge_"):
                    parts = tag.split("_")
                    u, v = int(parts[1]), int(parts[2])
                    self.show_edge_tooltip(event.x, event.y, u, v)
                    return

    def show_node_tooltip(self, x, y, nid):
        """Düğüm bilgilerini ve GERÇEK bağlantı sayısını gösterir."""
        if not hasattr(self, 'graph') or nid not in self.graph.nodes: return
        
        node = self.graph.nodes[nid]
        props = node.properties
        
        # Bağlantı Skoru artık JSON'daki sayıdan değil, gerçek komşu listesinden okunur
        gercek_baglanti = len(node.neighbors)
        
        text = (f"ID: {nid}\nİsim: {node.name}\n"
                f"Aktiflik: {props.get('aktiflik', 0)}\n"
                f"Etkileşim: {props.get('etkilesim', 0)}\n"
                f"Bağlantı Skoru: {gercek_baglanti}") # DÜZELTİLDİ
        
        self._create_tooltip_box(x, y, text, 95)

    def show_edge_tooltip(self, x, y, u, v):
        node_u = self.graph.nodes[u]
        node_v = self.graph.nodes[v]
        maliyet = abs(node_u.properties.get('aktiflik', 0) - node_v.properties.get('aktiflik', 0)) + 10
        text = f"Yol: {u} ↔ {v}\nMaliyet: {maliyet:.2f}"
        self._create_tooltip_box(x, y, text, 50)

    def _create_tooltip_box(self, x, y, text, h):
        ox, oy = 15, 15
        self.tooltip_rect = self.create_rectangle(
            x + ox, y + oy, x + ox + 160, y + oy + h, 
            fill="#fdf6e3", outline="#657b83", width=1
        )
        self.tooltip_text = self.create_text(
            x + ox + 8, y + oy + 8, 
            text=text, anchor="nw", 
            font=("Arial", 9), fill="#073642"
        )

    def hide_tooltip(self):
        if hasattr(self, 'tooltip_rect'):
            self.delete(self.tooltip_rect)
            delattr(self, 'tooltip_rect')
        if hasattr(self, 'tooltip_text'):
            self.delete(self.tooltip_text)
            delattr(self, 'tooltip_text')