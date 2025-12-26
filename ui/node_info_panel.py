import customtkinter as ctk

class NodeInfoPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=22, fg_color=("#ffffff", "#1a1c1e"), border_width=1, border_color="#2d2d2d")
        
        self.badge_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.badge_frame.pack(fill="x", padx=20, pady=(15, 5))
        
        self.container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True, padx=10, pady=5)

    def clear_panel(self):
        """Paneldeki eski verileri temizler."""
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_order(self, alg_name, order, graph):
        """BFS ve DFS ziyaret sırasını modern bir liste şeklinde gösterir."""
        self.clear_panel()
        
        title_icon = "🔍" if alg_name == "BFS" else "🔎"
        header = ctk.CTkLabel(self.container, text=f"{title_icon} {alg_name} TARAMA SONUCU", 
                              font=("Roboto", 15, "bold"), text_color="#3498db")
        header.pack(pady=(10, 20))

        list_header = ctk.CTkFrame(self.container, fg_color="#2d2d2d", height=35, corner_radius=8)
        list_header.pack(fill="x", padx=10, pady=(0, 10))
        ctk.CTkLabel(list_header, text="Adım", font=("Roboto", 11, "bold"), text_color="#95a5a6").pack(side="left", padx=15)
        ctk.CTkLabel(list_header, text="Ziyaret Edilen Düğüm", font=("Roboto", 11, "bold"), text_color="#95a5a6").pack(side="right", padx=15)

        for i, nid in enumerate(order, 1):
            row = ctk.CTkFrame(self.container, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=2)
            
            step_box = ctk.CTkLabel(row, text=f"{i}", font=("Roboto", 12, "bold"), 
                                    fg_color="#34495e", text_color="white", width=30, corner_radius=6)
            step_box.pack(side="left", padx=5)
            
            node_name = graph.nodes[nid].name if nid in graph.nodes else f"Düğüm {nid}"
            node_lbl = ctk.CTkLabel(row, text=f"{node_name}", font=("Roboto", 13))
            node_lbl.pack(side="left", padx=10)
            
            id_badge = ctk.CTkLabel(row, text=f"ID: {nid}", font=("Roboto", 11, "bold"), 
                                    text_color="#2ecc71", fg_color="#1e2f24", corner_radius=8, padx=10)
            id_badge.pack(side="right", padx=5)
            
            line = ctk.CTkFrame(self.container, fg_color="#2d2d2d", height=1)
            line.pack(fill="x", padx=15, pady=2)

    def show_path(self, alg_name, path, cost):
        """Dijkstra ve A* yol sonuçlarını modern bir rota şeklinde gösterir."""
        self.clear_panel()
        ctk.CTkLabel(self.container, text=f"📍 {alg_name} EN KISA YOL", 
                      font=("Roboto", 15, "bold"), text_color="#e74c3c").pack(pady=(10, 10))
        
        cost_frame = ctk.CTkFrame(self.container, fg_color="#c0392b", corner_radius=10)
        cost_frame.pack(pady=5)
        ctk.CTkLabel(cost_frame, text=f"TOPLAM MALİYET: {cost:.2f}", 
                    font=("Roboto", 12, "bold"), text_color="white", padx=15).pack()

        self.add_separator()
        
        for i, step in enumerate(path):
            row = ctk.CTkFrame(self.container, fg_color="transparent")
            row.pack(fill="x", padx=20)
            
            prefix = "🏁" if i == 0 else "↓"
            ctk.CTkLabel(row, text=prefix, font=("Roboto", 16)).pack(pady=2)
            
            step_lbl = ctk.CTkLabel(row, text=str(step), font=("Roboto", 13, "bold"), text_color="#ecf0f1")
            step_lbl.pack(pady=2)

    def show_degree_table(self, graph, sorted_list):
        """Merkeziyet tablosunda hem isim, hem ID, hem de bağlantı sayısını gösterir."""
        self.clear_panel()
        ctk.CTkLabel(self.container, text="📊 EN ETKİLİ 5 ÖĞRENCİ", 
                      font=("Roboto", 15, "bold"), text_color="#f1c40f").pack(pady=(10, 20))

        for i, (nid, val) in enumerate(sorted_list, 1):
            node = graph.nodes[nid]
            row = ctk.CTkFrame(self.container, fg_color="#1c1c1c", corner_radius=12)
            row.pack(fill="x", padx=10, pady=5, ipady=5)
            
            rank_lbl = ctk.CTkLabel(row, text=str(i), font=("Roboto", 18, "bold"), 
                                    text_color="#f1c40f", width=40)
            rank_lbl.pack(side="left", padx=10)
            
            name_lbl = ctk.CTkLabel(row, text=node.name, font=("Roboto", 13, "bold"), anchor="w")
            name_lbl.pack(side="left", padx=5)

            id_badge = ctk.CTkLabel(row, text=f"ID: {nid}", font=("Roboto", 11, "bold"), 
                                    text_color="#2ecc71", fg_color="#1e2f24", corner_radius=8, padx=10)
            id_badge.pack(side="left", padx=10)
            
            count = len(node.neighbors)
            badge = ctk.CTkLabel(row, text=f"{count} Bağlantı", font=("Roboto", 11, "bold"), 
                                 fg_color="#3498db", text_color="white", corner_radius=8, padx=10)
            badge.pack(side="right", padx=15)

    def show_components(self, groups):
        """Bağlı bileşen analizini modern kartlar halinde gösterir."""
        self.clear_panel()
        ctk.CTkLabel(self.container, text="🔗 BAĞLI BİLEŞEN ANALİZİ", 
                      font=("Roboto", 15, "bold"), text_color="#9b59b6").pack(pady=(10, 20))
        
        for i, group in enumerate(groups, 1):
            box = ctk.CTkFrame(self.container, fg_color="#1c1c1c", corner_radius=12, border_width=1, border_color="#2d2d2d")
            box.pack(fill="x", padx=10, pady=8, ipady=5)
            
            top_row = ctk.CTkFrame(box, fg_color="transparent")
            top_row.pack(fill="x", padx=12, pady=(8, 2))
            
            ctk.CTkLabel(top_row, text=f"TOPLULUK {i}", font=("Roboto", 12, "bold"), text_color="#9b59b6").pack(side="left")
            
            count_badge = ctk.CTkLabel(top_row, text=f"{len(group)} Üye", font=("Roboto", 10, "bold"), 
                                       fg_color="#34495e", text_color="white", corner_radius=6, padx=8)
            count_badge.pack(side="right")
            
            line = ctk.CTkFrame(box, fg_color="#2d2d2d", height=1)
            line.pack(fill="x", padx=12, pady=8)
            
            members_text = ", ".join(map(str, group))
            members_lbl = ctk.CTkLabel(box, text=members_text, font=("Roboto", 13), 
                                       wraplength=380, text_color="#ecf0f1", justify="left")
            members_lbl.pack(padx=15, pady=(2, 12), anchor="w")

    def add_separator(self):
        """İçeriğe yatay ayırıcı ekler."""
        line = ctk.CTkFrame(self.container, fg_color="#2d2d2d", height=2)
        line.pack(fill="x", padx=20, pady=10)

    def show_message(self, text):
        """Panelde basit bir bilgilendirme mesajı gösterir."""
        self.clear_panel()
        ctk.CTkLabel(self.container, text=text, font=("Roboto", 13), 
                    wraplength=200, text_color="#bdc3c7").pack(pady=50)
