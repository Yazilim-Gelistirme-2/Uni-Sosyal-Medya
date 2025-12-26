import json
import random
import math
from src.node import Node
from src.utils import get_dynamic_weight # Formülü buradan çağıracağız

class Graph:
    def __init__(self):
        # Düğümleri ID bazlı saklar
        self.nodes = {}

    def add_node(self, node):
        """Sisteme yeni bir düğüm ekler."""
        self.nodes[node.id] = node

    def add_edge(self, source_id, target_id):
        """İki düğüm arasında çift taraflı kenar (bağlantı) oluşturur."""
        if source_id in self.nodes and target_id in self.nodes:
            # Kaynak düğümün komşularına hedefi ekle
            if target_id not in self.nodes[source_id].neighbors:
                self.nodes[source_id].neighbors.append(target_id)
            # Hedef düğümün komşularına kaynağı ekle (unweighted/undirected başlangıç)
            if source_id not in self.nodes[target_id].neighbors:
                self.nodes[target_id].neighbors.append(source_id)

    def get_edge_weight(self, source_id, target_id):
        """
        Görsel 4.3'teki Dinamik Ağırlık formülünü kullanarak iki düğüm arasındaki maliyeti döner.
        Bu fonksiyon hem Dijkstra hem A* tarafından ağırlık hesaplamak için kullanılır.
        """
        if source_id not in self.nodes or target_id not in self.nodes:
            return float('inf')
        
        # utils içindeki hesaplama motorunu kullan
        return get_dynamic_weight(self.nodes[source_id], self.nodes[target_id])

    def load_from_json(self, json_file_path):
        """JSON dosyasından düğüm ve kenar verilerini yükler, eksik özellikleri rastgele tamamlar."""
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Düğümleri oluştur
        for node_data in data['nodes']:
            props = node_data.get('properties', {})
            # Eğer özellikler boşsa görseldeki isterlere göre (Aktiflik, Etkileşim, Bağlantı Sayısı) doldur
            if not props:
                props = {
                    "aktiflik": round(random.uniform(0.1, 1.0), 2), # 0.8 gibi değerler için
                    "etkilesim": random.randint(1, 50),             # 12 gibi değerler için
                    "baglanti_sayisi": random.randint(1, 15)        # 3 gibi değerler için
                }
            
            node = Node(
                id=node_data['id'], 
                name=node_data['name'], 
                properties=props
            )
            self.add_node(node)
            
        # Kenarları (Bağlantıları) oluştur
        for edge in data['edges']:
            self.add_edge(edge['source'], edge['target'])

    def get_adjacency_matrix(self):
        """
        Grafı hocanın istediği komşuluk matrisine (0-1 tablosuna) dönüştürür.
        CSV çıktısı almak için bu fonksiyon kullanılır.
        """
        nodes = sorted(list(self.nodes.keys()))
        size = len(nodes)
        # Sıfırlardan oluşan kare matris oluştur
        matrix = [[0] * size for _ in range(size)]
        
        # ID'leri matris indekslerine eşle
        id_to_idx = {nid: i for i, nid in enumerate(nodes)}
        
        for nid, node in self.nodes.items():
            for neighbor in node.neighbors:
                if neighbor in id_to_idx:
                    # Bağlantı varsa 1 işaretle
                    matrix[id_to_idx[nid]][id_to_idx[neighbor]] = 1
                    
        return nodes, matrix

    def get_node_count(self):
        """Toplam düğüm sayısını döner."""
        return len(self.nodes)

    def get_all_nodes(self):
        """Tüm düğüm nesnelerini liste olarak döner."""
        return list(self.nodes.values())
