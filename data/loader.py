import csv

def load_node_properties(graph, csv_path):
    """CSV verilerini düğüm özelliklerine (properties) eşler."""
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                node_id = int(row["DugumId"])
                if node_id in graph.nodes:
                    graph.nodes[node_id].properties = {
                        "aktiflik": float(row["Aktiflik"]),
                        "etkilesim": float(row["Etkilesim"]),
                        "baglanti_sayisi": int(row["BaglantiSayisi"])
                    }
    except FileNotFoundError:
        print(f"Hata: {csv_path} dosyası bulunamadı.")