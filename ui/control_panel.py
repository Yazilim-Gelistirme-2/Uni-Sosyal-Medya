import tkinter as tk
from tkinter import filedialog
from src.graph import Graph
from algorithms.centrality import Centrality
from algorithms.welsh_powell import WelshPowell

from algorithms.dfs import DFS

from algorithms.a_star import AStarAlgorithm
from tkinter import simpledialog, messagebox
from algorithms.a_star import AStarAlgorithm



class ControlPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=220, bg="#f0f0f0")

        tk.Label(self, text="Kontrol Paneli", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self, text="JSON Yükle", command=self.load_json).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(self, text="Degree Centrality", command=self.run_degree).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(self, text="Welsh–Powell", command=self.run_welsh_powell).pack(fill=tk.X, padx=10, pady=5)


        tk.Button(self, text="DFS", command=self.run_dfs).pack(fill=tk.X, padx=10, pady=5)

        tk.Button(self, text="A*", command=self.run_astar).pack(fill=tk.X, padx=10, pady=5)


    def load_json(self):
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not path:
            return

        self.master.graph = Graph()
        self.master.graph.load_from_json(path)

        self.master.graph_canvas.draw_graph(self.master.graph)
        self.master.node_info_panel.show_message("Graf başarıyla yüklendi.")

    def run_degree(self):
        graph = self.master.graph
        if not graph:
            return

        dc = Centrality.degree_centrality(graph)
        self.master.node_info_panel.show_degree_table(graph, dc)

    def run_welsh_powell(self):
        graph = self.master.graph
        if not graph:
            return

        colors = WelshPowell.color_graph(graph)
        self.master.graph_canvas.draw_graph(graph, colors)
        self.master.node_info_panel.show_color_table(graph, colors)

    """def run_bfs(self):
        graph = self.master.graph
        if not graph:
            return

        start = list(graph.nodes.keys())[0]
        order = BFS.run(graph, start)
        self.master.node_info_panel.show_order("BFS", order)"""

    def run_dfs(self):
        graph = self.master.graph
        if not graph:
            return

        start = list(graph.nodes.keys())[0]
        order = DFS.run(graph, start)
        self.master.node_info_panel.show_order("DFS", order)

    def run_astar(self):
        graph = self.master.graph
        if not graph:
            return

        # başlangıç düğümü (ilk düğüm)
        start = list(graph.nodes.keys())[0]

        # hedef düğüm input
        goal = simpledialog.askinteger(
            "A* Hedef Düğüm",
            "Hedef düğüm ID giriniz:"
        )

        if goal is None:
            return

        if goal not in graph.nodes:
            messagebox.showerror("Hata", "Geçersiz düğüm ID")
            return

        path, cost = AStarAlgorithm.run(graph, start, goal)

        if not path:
            self.master.node_info_panel.show_message("Yol bulunamadı")
            return

        self.master.node_info_panel.show_path("A*", path, cost)
        self.master.graph_canvas.draw_graph(graph, highlight_path=path)



