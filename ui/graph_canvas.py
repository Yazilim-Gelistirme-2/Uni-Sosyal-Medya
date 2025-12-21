import tkinter as tk
import math

class GraphCanvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, bg="white")

    def draw_graph(self, graph, colors=None, highlight_path=None):

        self.delete("all")

        n = len(graph.nodes)
        if n == 0:
            return

        radius = 220
        cx, cy = 500, 260

        positions = {}
        for i, node_id in enumerate(graph.nodes):
            angle = 2 * math.pi * i / n
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            positions[node_id] = (x, y)

        # Kenarlar
        for node_id, node in graph.nodes.items():
            for neighbor in node.neighbors:
                x1, y1 = positions[node_id]
                x2, y2 = positions[neighbor]
                self.create_line(x1, y1, x2, y2, fill="black")

        for node_id, node in graph.nodes.items():
            for neighbor in node.neighbors:
                x1, y1 = positions[node_id]
                x2, y2 = positions[neighbor]

                is_path = False
                if highlight_path:
                    for i in range(len(highlight_path) - 1):
                        if (highlight_path[i] == node_id and highlight_path[i + 1] == neighbor) or \
                                (highlight_path[i] == neighbor and highlight_path[i + 1] == node_id):
                            is_path = True
                            break

                if is_path:
                    self.create_line(x1, y1, x2, y2, width=4, fill="blue")
                else:
                    self.create_line(x1, y1, x2, y2, fill="black")

        # Düğümler
        color_map = {
            1: "#e74c3c",
            2: "#2ecc71",
            3: "#3498db",
            4: "#f1c40f",
            5: "#9b59b6"
        }
        fill = "lightgray"

        if highlight_path and node_id in highlight_path:
            fill = "#3498db"  # mavi
        elif colors:
            fill = color_map.get(colors[node_id], "gray")

        for node_id, (x, y) in positions.items():
            fill = "lightgray"
            if colors:
                fill = color_map.get(colors[node_id], "gray")

            self.create_oval(x-16, y-16, x+16, y+16, fill=fill)
            self.create_text(x, y, text=str(node_id), fill="white")
