import csv

def load_node_properties(graph, csv_path):
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                node_id = int(row["DugumId"])
                if node_id in graph.nodes:
                    # Tüm anahtarları küçük harfe zorlayarak kaydediyoruz
                    graph.nodes[node_id].properties = {
                        "aktiflik": float(row.get("Aktiflik", row.get("aktiflik", 0))),
                        "etkilesim": float(row.get("Etkilesim", row.get("etkilesim", 0))),
                        "baglanti_sayisi": int(row.get("BaglantiSayisi", row.get("baglanti_sayisi", 0)))
                    }
    except Exception as e:
        print(f"CSV Yükleme Hatası: {e}")