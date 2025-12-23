import customtkinter as ctk
import time
from tkinter import filedialog, simpledialog, messagebox
from algorithms.centrality import Centrality
from algorithms.welsh_powell import WelshPowell
from algorithms.bfs import aramaBFS
from algorithms.dijkstra import dijkstra
from algorithms.connected_components import BagliBilesenler
from algorithms.dfs import DFS
from algorithms.a_star import AStarAlgorithm
from src.graph import Graph


class ControlPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=15, fg_color=("#ebebeb", "#242424"))

        ctk.CTkLabel(self, text="📊 ANALİZ MERKEZİ", font=("Roboto", 18, "bold")).pack(pady=20)

        # Buton Oluşturma Yardımcısı
        def add_btn(text, command, section=None, color=None):
            if section:
                ctk.CTkLabel(self, text=section, font=("Roboto", 11, "bold"), text_color="gray").pack(pady=(15, 2),
                                                                                                      padx=20,
                                                                                                      anchor="w")
            btn = ctk.CTkButton(self, text=text, command=command, fg_color=color, corner_radius=8, height=35,
                                anchor="w")
            btn.pack(fill="x", padx=20, pady=4)
            return btn

        # Butonlar ve Bölümler
        add_btn("📁 JSON Veri Yükle", self.load_json, "VERİ MANAGEMENT", "#1f538d")

        add_btn("📉 Degree Centrality", self.run_degree, "AĞ ANALİZİ")
        add_btn("🔗 Bağlı Bileşenler", self.run_components)
        add_btn("🎨 Welsh–Powell Boyama", self.run_welsh_powell)

        add_btn("🔍 BFS Arama", self.run_bfs, "ARAMA VE YOL BULMA")
        add_btn("🔎 DFS Arama", self.run_dfs)
        add_btn("📍 Dijkstra (En Kısa Yol)", self.run_dijkstra)
        add_btn("🚀 A* Algoritması", self.run_astar)


    def measure_time(func):
        """Algoritma süresini ölçen dekoratör"""

        def wrapper(self, *args, **kwargs):
            if not self.master.graph:
                messagebox.showwarning("Uyarı", "Lütfen önce bir grafik dosyası yükleyin!")
                return False

            start_time = time.perf_counter()
            result = func(self, *args, **kwargs)
            end_time = time.perf_counter()

            if result is not False:
                ms = (end_time - start_time) * 1000
                self.master.node_info_panel.update_time(ms)
            return result

        return wrapper

    # --- Algoritma Fonksiyonları ---

    @measure_time
    def run_degree(self):
        dc = Centrality.degree_centrality(self.master.graph)
        self.master.node_info_panel.show_degree_table(self.master.graph, dc)

    @measure_time
    def run_welsh_powell(self):
        colors = WelshPowell.color_graph(self.master.graph)
        self.master.graph_canvas.draw_graph(self.master.graph, colors)
        self.master.node_info_panel.show_color_table(self.master.graph, colors)

    @measure_time
    def run_components(self):
        cc = BagliBilesenler(self.master.graph)
        sonuc = cc.calistir()
        self.master.node_info_panel.show_components(sonuc["gruplar"])
        self.master.graph_canvas.draw_graph(self.master.graph)

    @measure_time
    def run_bfs(self):
        start = simpledialog.askinteger("BFS", "Başlangıç Düğüm ID:")
        if start is None or start not in self.master.graph.nodes: return False
        bfs = aramaBFS(self.master.graph)
        sonuc = bfs.calistir(start)
        self.master.node_info_panel.show_order("BFS", sonuc["sonuc"])
        self.master.graph_canvas.draw_graph(self.master.graph)

    @measure_time
    def run_dfs(self):
        start = simpledialog.askinteger("DFS", "Başlangıç Düğüm ID:")
        if start is None or start not in self.master.graph.nodes: return False
        order = DFS.run(self.master.graph, start)
        self.master.node_info_panel.show_order("DFS", order)
        self.master.graph_canvas.draw_graph(self.master.graph)

    @measure_time
    def run_dijkstra(self):
        s = simpledialog.askinteger("Dijkstra", "Başlangıç ID:")
        g = simpledialog.askinteger("Dijkstra", "Hedef ID:")
        if s is None or g is None: return False

        dj = dijkstra(self.master.graph)
        res = dj.calistir(s, g)

        if "en_kisa_yol" in res:
            p_ids = [int(x.split("(")[1][:-1]) for x in res["en_kisa_yol"]]
            self.master.node_info_panel.show_path("Dijkstra", res["en_kisa_yol"], res["mesafe"])
            self.master.graph_canvas.draw_graph(self.master.graph, highlight_path=p_ids)
        else:
            self.master.node_info_panel.show_message("Yol bulunamadı!")

    @measure_time
    def run_astar(self):
        s = simpledialog.askinteger("A*", "Başlangıç ID:")
        g = simpledialog.askinteger("A*", "Hedef ID:")
        if s is None or g is None: return False

        path, cost = AStarAlgorithm.run(self.master.graph, s, g)
        if path:
            self.master.node_info_panel.show_path("A*", path, cost)
            self.master.graph_canvas.draw_graph(self.master.graph, highlight_path=path)
        else:
            self.master.node_info_panel.show_message("Yol bulunamadı!")

    # control_panel.py içindeki load_json fonksiyonunu güncelle:
    def load_json(self):
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not path: return

        # 1. Grafı Yükle
        self.master.graph = Graph()
        self.master.graph.load_from_json(path)

        # 2. Otomatik CSV Eşleşmesi (Dosya adından CSV bulma)
        # Örnek: data_samples/medium_data.json -> data_samples/medium_nodes.csv
        csv_path = path.replace("_data.json", "_nodes.csv")

        try:
            from data.loader import load_node_properties
            load_node_properties(self.master.graph, csv_path)
            status_msg = f"Graf ve Özellikler ({csv_path.split('/')[-1]}) Yüklendi."
        except Exception as e:
            status_msg = "Graf yüklendi ama CSV bulunamadı!"
            print(f"CSV Hatası: {e}")

        self.master.graph_canvas.draw_graph(self.master.graph)
        self.master.node_info_panel.show_message(status_msg)