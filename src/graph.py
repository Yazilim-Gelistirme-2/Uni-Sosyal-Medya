import json
import random
from src.node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, source_id, target_id):
        if source_id in self.nodes and target_id in self.nodes:
            if target_id not in self.nodes[source_id].neighbors:
                self.nodes[source_id].neighbors.append(target_id)
            if source_id not in self.nodes[target_id].neighbors:
                self.nodes[target_id].neighbors.append(source_id)

    def load_from_json(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for node_data in data['nodes']:
            props = node_data.get('properties', {})
            if not props:
                props = {
                    "aktiflik": random.randint(10, 100),
                    "etkilesim": random.randint(5, 50),
                    "baglanti_sayisi": 0
                }
            node = Node(id=node_data['id'], name=node_data['name'], properties=props)
            self.add_node(node)
        for edge in data['edges']:
            self.add_edge(edge['source'], edge['target'])

    def get_adjacency_matrix(self):
        """Grafı hocanın istediği komşuluk matrisine (0-1 tablosuna) dönüştürür."""
        nodes = sorted(list(self.nodes.keys()))
        size = len(nodes)
        matrix = [[0] * size for _ in range(size)]
        id_to_idx = {nid: i for i, nid in enumerate(nodes)}
        for nid, node in self.nodes.items():
            for neighbor in node.neighbors:
                if neighbor in id_to_idx:
                    matrix[id_to_idx[nid]][id_to_idx[neighbor]] = 1
        return nodes, matrix