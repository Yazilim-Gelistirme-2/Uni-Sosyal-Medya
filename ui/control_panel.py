import customtkinter as ctk
import time
import math
import json
import os
import random
from tkinter import filedialog, simpledialog, messagebox

from algorithms.centrality import Centrality
from algorithms.welsh_powell import WelshPowell
from algorithms.bfs import aramaBFS
from algorithms.dijkstra import dijkstra
from algorithms.connected_components import BagliBilesenler
from algorithms.dfs import DFS
from algorithms.a_star import AStarAlgorithm

class ControlPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="#0D1117", width=280)
        self.current_file_path = None 
        self.setup_ui()

    def setup_ui(self):
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.add_header("DATA MANAGEMENT")
        self.add_menu_item("Veri Seti Yükle", self.load_json, "📁")
        self.add_menu_item("Yeni Öğrenci Ekle", self.add_node_ui, "➕")
        self.add_menu_item("Bilgileri Güncelle", self.update_node_ui, "📝")
        self.add_menu_item("Öğrenci Kaydı Sil", self.delete_node_ui, "❌")
        self.add_menu_item("Bağlantı Kur", self.add_edge_ui, "🤝")
        self.add_menu_item("Değişiklikleri Kaydet", self.save_to_json, "💾")
        # Hocanın istediği yeni özellik buraya eklendi, diğerleri kaydırıldı
        self.add_menu_item("Matrisi CSV Yap", self.export_matrix_csv, "📊")

        self.add_header("AĞ ANALİZİ")
        self.add_menu_item("Merkeziyet (Centrality)", self.run_degree, "📊")
        self.add_menu_item("Bağlı Bileşenler", self.run_components, "🔗")
        self.add_menu_item("Welsh–Powell Boyama", self.run_welsh_powell, "🎨")

        self.add_header("YOL BULMA VE TARAMA")
        self.add_menu_item("Dijkstra (En Kısa Yol)", self.run_dijkstra, "📍")
        self.add_menu_item("A* Algoritması", self.run_astar, "🚀")
        self.add_menu_item("BFS Taraması", self.run_bfs, "🔍")
        self.add_menu_item("DFS Taraması", self.run_dfs, "🔎")

    def add_header(self, title):
        lbl = ctk.CTkLabel(self.scroll_frame, text=title, font=("Inter", 10, "bold"), text_color="#484F58", anchor="w")
        lbl.pack(fill="x", padx=20, pady=(15, 5))

    def add_menu_item(self, text, command, icon):
        btn = ctk.CTkButton(self.scroll_frame, text=f"  {icon}  {text}", command=command,
                            anchor="w", fg_color="transparent", hover_color="#1C2128",
                            text_color="#C9D1D9", font=("Inter", 12), height=40, corner_radius=8)
        btn.pack(fill="x", padx=10, pady=2)

    # --- HOCANIN İSTEDİĞİ MATRİS DIŞA AKTARIMI ---
    def export_matrix_csv(self):
        """Grafın komşuluk matrisini CSV olarak kaydeder."""
        if not self.master.graph: 
            messagebox.showwarning("Uyarı", "Önce bir veri seti yüklemelisiniz!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
            title="Komşuluk Matrisini Kaydet"
        )
        
        if file_path:
            try:
                nodes, matrix = self.master.graph.get_adjacency_matrix()
                with open(file_path, 'w', encoding='utf-8') as f:
                    # Başlık satırı
                    f.write("," + ",".join(map(str, nodes)) + "\n")
                    # Veri satırları
                    for i, row in enumerate(matrix):
                        f.write(f"{nodes[i]}," + ",".join(map(str, row)) + "\n")
                messagebox.showinfo("Başarılı", "Matris CSV olarak dışa aktarıldı!")
            except Exception as e:
                messagebox.showerror("Hata", f"İşlem başarısız: {str(e)}")

    def _safe_extract_ids(self, path_list):
        p_ids = []
        for x in path_list:
            if isinstance(x, str) and "(" in x:
                p_ids.append(int(x.split("(")[1][:-1]))
            else:
                p_ids.append(int(x))
        return p_ids

    def run_astar(self):
        if not self.master.graph: return
        s, g = simpledialog.askinteger("A*", "Başlangıç:"), simpledialog.askinteger("A*", "Hedef:")
        if s is not None and g is not None:
            path, cost = AStarAlgorithm.run(self.master.graph, s, g)
            if path:
                self.master.node_info_panel.show_path("A*", path, cost)
                p_ids = self._safe_extract_ids(path)
                self.master.graph_canvas.draw_graph(self.master.graph, highlight_path=p_ids)

    def run_dijkstra(self):
        if not self.master.graph: return
        s, g = simpledialog.askinteger("Dijkstra", "Başlangıç:"), simpledialog.askinteger("Dijkstra", "Hedef:")
        if s is not None and g is not None:
            res = dijkstra(self.master.graph).calistir(s, g)
            if "en_kisa_yol" in res:
                self.master.node_info_panel.show_path("Dijkstra", res["en_kisa_yol"], res["mesafe"])
                p_ids = self._safe_extract_ids(res["en_kisa_yol"])
                self.master.graph_canvas.draw_graph(self.master.graph, highlight_path=p_ids)

    def run_bfs(self):
        if not self.master.graph: return
        start = simpledialog.askinteger("BFS", "Başlangıç ID:")
        if start:
            res = aramaBFS(self.master.graph).calistir(start)
            self.master.node_info_panel.show_order("BFS", res["sonuc"], self.master.graph)
            self.master.graph_canvas.draw_graph(self.master.graph)

    def run_dfs(self):
        if not self.master.graph: return
        start = simpledialog.askinteger("DFS", "Başlangıç ID:")
        if start and start in self.master.graph.nodes:
            order = DFS.run(self.master.graph, start)
            self.master.node_info_panel.show_order("DFS", order, self.master.graph)
            self.master.graph_canvas.draw_graph(self.master.graph)

    def load_json(self):
        from src.graph import Graph
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            self.current_file_path = path
            self.master.graph = Graph()
            self.master.graph.load_from_json(path)
            self.master.graph_canvas.draw_graph(self.master.graph)

    def save_to_json(self):
        if not self.master.graph or not self.current_file_path: return
        try:
            data = {"nodes": [], "edges": []}
            for nid, node in self.master.graph.nodes.items():
                data["nodes"].append({"id": nid, "name": node.name, "properties": node.properties})
                for neighbor in node.neighbors:
                    if nid < neighbor: data["edges"].append({"source": nid, "target": neighbor})
            with open(self.current_file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("Başarılı", "💾 Kaydedildi!")
        except Exception as e: messagebox.showerror("Hata", str(e))

    def update_node_ui(self):
        if not self.master.graph: return
        nid = simpledialog.askinteger("Güncelle", "ID:")
        if nid in self.master.graph.nodes:
            node = self.master.graph.nodes[nid]
            new_name = simpledialog.askstring("İsim", "Yeni:", initialvalue=node.name)
            try:
                a = simpledialog.askinteger("Puan", "Aktiflik:", initialvalue=node.properties.get("aktiflik", 50))
                e = simpledialog.askinteger("Puan", "Etkileşim:", initialvalue=node.properties.get("etkilesim", 20))
                b = len(node.neighbors)
                node.name = new_name
                node.properties = {"aktiflik": a, "etkilesim": e, "baglanti_sayisi": b}
                self.master.graph_canvas.draw_graph(self.master.graph)
            except: pass

    def run_degree(self):
        if not self.master.graph: return
        top_5 = Centrality.top_k_degree_nodes(self.master.graph, k=5)
        self.master.node_info_panel.show_degree_table(self.master.graph, top_5)

    def run_components(self):
        if not self.master.graph: return
        res = BagliBilesenler(self.master.graph).calistir()
        self.master.node_info_panel.show_components(res["gruplar"])

    def run_welsh_powell(self):
        if not self.master.graph: return
        colors = WelshPowell.color_graph(self.master.graph)
        self.master.graph_canvas.draw_graph(self.master.graph, colors)
        self.master.node_info_panel.show_message("🎨 Boyama Tamamlandı!")

    def add_node_ui(self):
        if not self.master.graph: return
        new_id = simpledialog.askinteger("Yeni", "ID:")
        if new_id is not None:
            if new_id in self.master.graph.nodes:
                messagebox.showerror("Hata", "ID kullanımda!")
                return
            name = simpledialog.askstring("Yeni", "Ad Soyad:")
            if name:
                from src.graph import Node
                self.master.graph.nodes[new_id] = Node(new_id, name, properties={"aktiflik": 50, "etkilesim": 20, "baglanti_sayisi": 0})
                self.master.graph_canvas.positions = {}
                self.master.graph_canvas.draw_graph(self.master.graph)

    def delete_node_ui(self):
        if not self.master.graph: return
        nid = simpledialog.askinteger("Sil", "ID:")
        if nid in self.master.graph.nodes:
            for n in self.master.graph.nodes.values():
                if nid in n.neighbors: n.neighbors.remove(nid)
            del self.master.graph.nodes[nid]
            self.master.graph_canvas.positions = {}
            self.master.graph_canvas.delete("all")
            self.master.graph_canvas.draw_graph(self.master.graph)

    def add_edge_ui(self):
        if not self.master.graph: return
        id1, id2 = simpledialog.askinteger("Bağ", "ID 1:"), simpledialog.askinteger("Bağ", "ID 2:")
        if id1 and id2 and id1 in self.master.graph.nodes and id2 in self.master.graph.nodes:
            if id2 not in self.master.graph.nodes[id1].neighbors:
                self.master.graph.nodes[id1].neighbors.append(id2)
                self.master.graph.nodes[id2].neighbors.append(id1)
                self.master.graph_canvas.draw_graph(self.master.graph)