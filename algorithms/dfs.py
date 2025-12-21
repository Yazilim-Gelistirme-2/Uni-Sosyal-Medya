class DFS:
    @staticmethod
    def run(graph, start_id):
        visited = set()
        stack = [start_id]
        order = []

        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                order.append(u)
                for v in reversed(graph.nodes[u].neighbors):
                    if v not in visited:
                        stack.append(v)

        return order
