
from src.graph import Graph
from algorithms.welsh_powell import WelshPowell
from ui.main_window import MainWindow
graph = Graph()
graph.load_from_json("data_samples/small_data.json")

colors = WelshPowell.color_graph(graph)


for node_id, node in graph.nodes.items():
    for neighbor_id in node.neighbors:
        if colors[node_id] == colors[neighbor_id]:
            print("❌ HATA:", node_id, "ile", neighbor_id, "aynı renkte")
            break
else:
    print("✅ TEST BAŞARILI: Komşu düğümler farklı renkte")

    print("\nWelsh–Powell Boyama Tablosu\n")
    print(f"{'ID':<5}{'İsim':<10}{'Komşular':<20}{'Renk'}")
    print("-" * 45)

    for node_id, color in colors.items():
        node = graph.nodes[node_id]
        print(f"{node_id:<5}{node.name:<10}{str(node.neighbors):<20}{color}")




def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()