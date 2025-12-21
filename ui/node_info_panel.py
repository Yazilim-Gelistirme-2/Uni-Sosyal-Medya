import tkinter as tk
from tkinter import ttk

class NodeInfoPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=200)

        self.tree = ttk.Treeview(self, columns=("col1","col2","col3"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def clear(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def show_message(self, message):
        self.clear()
        self.tree["columns"] = ("msg",)
        self.tree.heading("msg", text=message)

    def show_degree_table(self, graph, dc):
        self.clear()
        self.tree["columns"] = ("id","name","degree","centrality")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="İsim")
        self.tree.heading("degree", text="Derece")
        self.tree.heading("centrality", text="Degree Centrality")

        for node_id, value in dc.items():
            node = graph.nodes[node_id]
            self.tree.insert("", "end", values=(
                node_id,
                node.name,
                len(node.neighbors),
                f"{value:.3f}"
            ))

    def show_color_table(self, graph, colors):
        self.clear()
        self.tree["columns"] = ("id","name","color")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="İsim")
        self.tree.heading("color", text="Renk")

        for node_id, color in colors.items():
            node = graph.nodes[node_id]
            self.tree.insert("", "end", values=(
                node_id,
                node.name,
                f"Renk {color}"
            ))

    def show_order(self, title, order):
        self.clear()
        self.tree["columns"] = ("step", "node")
        self.tree.heading("step", text="Adım")
        self.tree.heading("node", text=f"{title} Sırası")

        for i, node in enumerate(order):
            self.tree.insert("", "end", values=(i + 1, node))

    def show_path(self, title, path, cost):
        self.clear()
        self.tree["columns"] = ("info",)
        self.tree.heading("info", text=f"{title} | Maliyet: {cost}")

        for node in path:
            self.tree.insert("", "end", values=(node,))

    def show_distance_table(self, graph, dist):
        self.clear()
        self.tree["columns"] = ("id", "name", "distance")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="İsim")
        self.tree.heading("distance", text="Mesafe")

        for node_id, d in dist.items():
            node = graph.nodes[node_id]
            self.tree.insert("", "end", values=(
                node_id,
                node.name,
                "∞" if d == float("inf") else d
            ))

    def show_components(self, components):
        self.clear()
        self.tree["columns"] = ("component", "nodes")
        self.tree.heading("component", text="Bileşen")
        self.tree.heading("nodes", text="Düğümler")

        for i, comp in enumerate(components):
            self.tree.insert("", "end", values=(
                f"Bileşen {i + 1}",
                ", ".join(map(str, comp))
            ))




