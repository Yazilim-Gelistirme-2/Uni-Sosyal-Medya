import customtkinter as ctk
from ui.control_panel import ControlPanel
from ui.graph_canvas import GraphCanvas
from ui.node_info_panel import NodeInfoPanel

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KOU Sosyal Ağ Analizörü v2.0")
        self.geometry("1280x850")
        ctk.set_appearance_mode("dark")

        self.graph = None

        # Grid Yapılandırması
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.control_panel = ControlPanel(self)
        self.control_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.right_container = ctk.CTkFrame(self, fg_color="transparent")
        self.right_container.grid(row=0, column=1, sticky="nsew", padx=(0,10), pady=10)
        self.right_container.grid_rowconfigure(0, weight=3) # Canvas alanı
        self.right_container.grid_rowconfigure(1, weight=1) # Tablo alanı
        self.right_container.grid_columnconfigure(0, weight=1)

        self.graph_canvas = GraphCanvas(self.right_container)
        self.graph_canvas.grid(row=0, column=0, sticky="nsew", pady=(0,10))

        self.node_info_panel = NodeInfoPanel(self.right_container)
        self.node_info_panel.grid(row=1, column=0, sticky="nsew")