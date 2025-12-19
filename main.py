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
print("-" * 30)