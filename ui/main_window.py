import customtkinter as ctk
from ui.control_panel import ControlPanel
from ui.graph_canvas import GraphCanvas
from ui.node_info_panel import NodeInfoPanel

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KOU | Network Intelligence")
        self.geometry("1500x900")
        self.configure(fg_color="#010409")

        self.grid_columnconfigure(0, weight=0, minsize=280) 
        self.grid_columnconfigure(1, weight=2) 
        self.grid_columnconfigure(2, weight=1, minsize=450) 
        
        self.grid_rowconfigure(0, weight=1)

        self.control_panel = ControlPanel(self)
        self.control_panel.grid(row=0, column=0, sticky="nsew")

        
        self.graph_card = ctk.CTkFrame(self, corner_radius=15, fg_color="white", border_width=1, border_color="#30363D")
        self.graph_card.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        
        self.graph_canvas = GraphCanvas(self.graph_card)
        self.graph_canvas.pack(fill="both", expand=True, padx=2, pady=2)

        self.node_info_panel = NodeInfoPanel(self)
        self.node_info_panel.grid(row=0, column=2, sticky="nsew", padx=(0, 25), pady=25)
        
        self.graph = None
