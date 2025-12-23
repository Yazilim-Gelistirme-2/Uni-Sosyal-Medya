class Centrality:

    @staticmethod
    def degree_centrality(graph):
        n = len(graph.nodes)
        centrality = {}

        for node_id, node in graph.nodes.items():
            centrality[node_id] = len(node.neighbors) / (n - 1)

        return centrality

    @staticmethod
    def top_k_degree_nodes(graph, k=5):

        dc = Centrality.degree_centrality(graph)


        sorted_nodes = sorted(
            dc.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_nodes[:k]
