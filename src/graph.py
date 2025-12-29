import json
import random
import math
from src.node import Node
from src.utils import get_dynamic_weight


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

    def get_edge_weight(self, source_id, target_id):
        if source_id not in self.nodes or target_id not in self.nodes:
            return float('inf')

        return get_dynamic_weight(self.nodes[source_id], self.nodes[target_id])

    def load_from_json(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Düğümleri oluştur
        for node_data in data['nodes']:
            props = node_data.get('properties', {})
            if not props:
                props = {
                    "aktiflik": round(random.uniform(0.1, 1.0), 2),
                    "etkilesim": random.randint(1, 50),
                    "baglanti_sayisi": random.randint(1, 15)
                }

            node = Node(
                id=node_data['id'],
                name=node_data['name'],
                properties=props
            )
            self.add_node(node)
        for edge in data['edges']:
            self.add_edge(edge['source'], edge['target'])

    def get_adjacency_matrix(self):
        nodes = sorted(list(self.nodes.keys()))
        size = len(nodes)
        matrix = [[0] * size for _ in range(size)]
        id_to_idx = {nid: i for i, nid in enumerate(nodes)}

        for nid, node in self.nodes.items():
            for neighbor in node.neighbors:
                if neighbor in id_to_idx:
                    matrix[id_to_idx[nid]][id_to_idx[neighbor]] = 1

        return nodes, matrix

    def get_node_count(self):
        return len(self.nodes)

    def get_all_nodes(self):
        return list(self.nodes.values())