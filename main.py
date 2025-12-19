"""from algorithms.dfs import DFS
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

from src.graph import Graph
from data.loader import load_node_properties
from algorithms.a_star import AStarAlgorithm

graph = Graph()
graph.load_from_json("data_samples/small_data.json")

# 🔥 CSV burada gerçekten kullanılıyor
load_node_properties(graph, "data_samples/nodes.csv")

astar = AStarAlgorithm()
path = astar.run(graph, 1, 14)

print("A* En Kısa Yol:")
for node in path:
    print(f"{node.id} - {node.name}")

