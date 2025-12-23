import json
import csv
import random

# 60 Düğümlü Orta Ölçekli Graf
node_count = 60
nodes_data = []
csv_data = []
edges = []

departments = ["Bilişim", "Elektrik", "Makine", "İnşaat", "Endüstri"]

# Düğümleri ve CSV Özelliklerini Oluştur
for i in range(1, node_count + 1):
    nodes_data.append({
        "id": i,
        "name": f"User_{i}",
        "department": random.choice(departments)
    })

    csv_data.append({
        "DugumId": i,
        "Aktiflik": round(random.uniform(0.1, 1.0), 2),
        "Etkilesim": random.randint(1, 50),
        "BaglantiSayisi": 0  # Aşağıda hesaplanacak
    })

# Rastgele Bağlantılar (Edges) Oluştur
# Her düğümü en az 1-3 yere bağlayalım ki kopuk olmasın
for i in range(1, node_count + 1):
    targets = random.sample(range(1, node_count + 1), random.randint(1, 3))
    for t in targets:
        if i != t:
            edge = tuple(sorted((i, t)))
            if edge not in edges:
                edges.append(edge)

# Bağlantı sayılarını güncelle
for s, t in edges:
    csv_data[s - 1]["BaglantiSayisi"] += 1
    csv_data[t - 1]["BaglantiSayisi"] += 1

# JSON Kaydet
json_output = {
    "graph_info": {"name": "KOU Medium Network", "node_count": node_count, "type": "undirected"},
    "nodes": nodes_data,
    "edges": [{"source": s, "target": t} for s, t in edges]
}

with open("data_samples/medium_data.json", "w", encoding="utf-8") as f:
    json.dump(json_output, f, ensure_ascii=False, indent=4)

# CSV Kaydet
with open("data_samples/medium_nodes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["DugumId", "Aktiflik", "Etkilesim", "BaglantiSayisi"])
    writer.writeheader()
    writer.writerows(csv_data)

print("Orta ölçekli test dosyaları hazır!")