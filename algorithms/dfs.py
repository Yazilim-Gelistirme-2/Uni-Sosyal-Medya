class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.path = []

    def solve(self, start_node):
        self.visited.clear()
        self.path.clear()

        if start_node in self.graph.nodes:
            self._traverse(start_node)
        return self.path

    def _traverse(self, node_id):
        self.visited.add(node_id)

        node = self.graph.nodes[node_id]
        self.path.append(node)

        for neighbor in node.neighbors:
            if neighbor not in self.visited:
                self._traverse(neighbor)