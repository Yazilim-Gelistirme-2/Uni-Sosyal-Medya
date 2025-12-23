import json
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
            node = Node(
                id=node_data['id'],
                name=node_data['name'],
                properties=node_data.get('properties', {})
            )
            self.add_node(node)

        for edge in data['edges']:
            self.add_edge(edge['source'], edge['target'])

        print(f"Graf yüklendi: {len(self.nodes)} düğüm.")
