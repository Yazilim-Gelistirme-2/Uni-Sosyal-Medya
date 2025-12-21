import tkinter as tk
from ui.control_panel import ControlPanel
from ui.graph_canvas import GraphCanvas
from ui.node_info_panel import NodeInfoPanel

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("KOU Graf Algoritmaları")
        self.geometry("1100x650")

        self.graph = None

        self.control_panel = ControlPanel(self)
        self.control_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.graph_canvas = GraphCanvas(self)
        self.graph_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.node_info_panel = NodeInfoPanel(self)
        self.node_info_panel.pack(side=tk.BOTTOM, fill=tk.X)
