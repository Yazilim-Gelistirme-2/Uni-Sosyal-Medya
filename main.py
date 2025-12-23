"""
DFS algoritması
from algorithms.dfs import DFS
from src.graph import Graph

social_graph=Graph()

try:
    social_graph.load_from_json("data_samples/small_data.json")
except FileNotFoundError:
    print("JSON dosyası bulunamadı, lütfen dosyayı oluşturun.")


dfs = DFS(social_graph)
path = dfs.solve(6)


print("-" * 30)
print(f"DFS Ziyaret Sırası (Toplam {len(path)} düğüm):")
for node in path:
    print(f"ID: {node.id} - {node.name}")
print("-" * 30)"""

"""
A* algoritması
from src.graph import Graph
from data.loader import load_node_properties
from algorithms.a_star import AStarAlgorithm

graph = Graph()
graph.load_from_json("data_samples/small_data.json")

# 🔥 CSV burada gerçekten kullanılıyor
load_node_properties(graph, "data_samples/small_nodes.csv")

astar = AStarAlgorithm()
path = astar.run(graph, 1, 14)

print("A* En Kısa Yol:")
for node in path:
    print(f"{node.id} - {node.name}")
"""
"""
Degree Centrality
from src.graph import Graph
from algorithms.centrality import Centrality

graph = Graph()
graph.load_from_json("data_samples/small_data.json")

top5 = Centrality.top_k_degree_nodes(graph)

print("\nEn Etkili 5 Kullanıcı (Degree Centrality)\n")
print(f"{'Sıra':<5}{'ID':<5}{'İsim':<10}{'Derece':<10}{'Centrality'}")
print("-" * 45)

for i, (node_id, centrality) in enumerate(top5, start=1):
    node = graph.nodes[node_id]
    degree = len(node.neighbors)
    print(f"{i:<5}{node_id:<5}{node.name:<10}{degree:<10}{centrality:.3f}")
"""

"""
from src.graph import Graph
from algorithms.welsh_powell import WelshPowell
from ui.main_window import MainWindow
graph = Graph()
graph.load_from_json("data_samples/small_data.json")

colors = WelshPowell.color_graph(graph)

# Komşular aynı renkte mi kontrol et
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
"""

"""
BFS
from src.graph import Graph
from algorithms.bfs import aramaBFS

graph = Graph()
graph.load_from_json("data_samples/small_data.json")  

bfs = aramaBFS(graph)                   
sonuc = bfs.calistir(1)

print(sonuc)
"""

"""
Dijkstra
from src.graph import Graph
from algorithms.dijkstra import dijkstra

graph = Graph()
graph.load_from_json("data_samples/small_data.json")

dj = dijkstra(graph)
sonuc = dj.calistir(1, 5)

print(sonuc)
"""

"""
Connected Component
from src.graph import Graph
from src.graph import Graph
from algorithms.connected_components import BagliBilesenler

graph = Graph()
graph.load_from_json("data_samples/small_data.json")

bb = BagliBilesenler(graph)
sonuc = bb.calistir()

print("Bağlı Bileşenler:")
for i, grup in enumerate(sonuc["gruplar"], 1):
    print(f"{i}. Grup:", grup)

print("Toplam Grup:", sonuc["adet"])
print("Süre:", sonuc["sure"], "sn")
"""



from src.graph import Graph
from algorithms.welsh_powell import WelshPowell
from ui.main_window import MainWindow
graph = Graph()
graph.load_from_json("data_samples/small_data.json")

colors = WelshPowell.color_graph(graph)

# Komşular aynı renkte mi kontrol et
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
