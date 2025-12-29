import customtkinter as ctk
from tkinter import ttk


class NodeInfoPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=220, corner_radius=15, fg_color=("#ffffff", "#2b2b2b"))

        self.info_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.info_bar.pack(fill="x", padx=15, pady=5)

        self.status_label = ctk.CTkLabel(self.info_bar, text="Sistem Hazır", font=("Roboto", 13, "bold"))
        self.status_label.pack(side="left")

        self.time_badge = ctk.CTkLabel(self.info_bar, text="⏱ 0.0000 ms",
                                       fg_color="#27ae60", text_color="white",
                                       corner_radius=5, padx=10)
        self.time_badge.pack(side="right")

        self.setup_treeview_style()

        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def setup_treeview_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#333333",
                        foreground="white",
                        fieldbackground="#333333",
                        rowheight=28,
                        font=("Roboto", 10))
        style.map("Treeview", background=[('selected', '#1f538d')])
        style.configure("Treeview.Heading", font=("Roboto", 11, "bold"))

    def clear(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def update_time(self, ms):
        self.time_badge.configure(text=f"⏱ {ms:.4f} ms")

    def show_message(self, msg):
        self.status_label.configure(text=msg)


    def show_order(self, title, order):
        self.clear()
        self.show_message(f"{title} Ziyaret Sıralaması")
        self.tree["columns"] = ("step", "node")
        self.tree.heading("step", text="Adım")
        self.tree.heading("node", text="Düğüm (ID)")

        for i, node in enumerate(order):
            self.tree.insert("", "end", values=(i + 1, node))

    def show_path(self, title, path, cost):
        self.clear()
        self.status_label.configure(
            text=f"🚀 {title} Analizi Tamamlandı | Toplam Yol Maliyeti: {cost:.4f}",
            text_color="#e67e22"
        )
        self.tree["columns"] = ("index", "node")
        self.tree.heading("index", text="Sıra")
        self.tree.heading("node", text="Yol Üzerindeki Düğüm")

        for i, node in enumerate(path):
            self.tree.insert("", "end", values=(i + 1, node))

    def show_degree_table(self, graph, dc):
        self.clear()
        self.show_message("Degree Centrality Analizi")
        self.tree["columns"] = ("id", "name", "degree", "centrality")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="İsim")
        self.tree.heading("degree", text="Derece")
        self.tree.heading("centrality", text="Merkeziyet")

        for node_id, value in dc.items():
            node = graph.nodes[node_id]
            self.tree.insert("", "end", values=(
                node_id, node.name, len(node.neighbors), f"{value:.4f}"
            ))

    def show_color_table(self, graph, colors):
        self.clear()
        self.show_message("Welsh-Powell Graf Boyama")
        self.tree["columns"] = ("id", "name", "color")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="İsim")
        self.tree.heading("color", text="Atanan Renk Grubu")

        for node_id, color_idx in colors.items():
            node = graph.nodes[node_id]
            self.tree.insert("", "end", values=(node_id, node.name, f"Grup {color_idx}"))

    def show_components(self, components):
        self.clear()
        self.show_message(f"Bağlı Bileşen Analizi ({len(components)} Grup Bulundu)")
        self.tree["columns"] = ("comp", "nodes")
        self.tree.heading("comp", text="Bileşen")
        self.tree.heading("nodes", text="Düğümler")

        for i, comp in enumerate(components):
            self.tree.insert("", "end", values=(f"Grup {i + 1}", ", ".join(map(str, comp))))
