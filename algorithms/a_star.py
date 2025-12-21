import heapq


class AStarAlgorithm:
    def __init__(self):
        self.open_set = []
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

    def calculate_weight(self, node_i, node_j):
        return 1 / (
            1 +
            (node_i.properties["aktiflik"] - node_j.properties["aktiflik"]) ** 2 +
            (node_i.properties["etkilesim"] - node_j.properties["etkilesim"]) ** 2 +
            (node_i.properties["baglanti_sayisi"] - node_j.properties["baglanti_sayisi"]) ** 2
        )

    def heuristic(self, node, goal):
        return abs(node.properties["aktiflik"] - goal.properties["aktiflik"])

    def reconstruct_path(self, current, graph):
        path = []
        while current in self.came_from:
            path.append(graph.nodes[current])
            current = self.came_from[current]
        path.append(graph.nodes[current])
        return path[::-1]

    def run(self, graph, start_id, goal_id):
        self.open_set.clear()
        self.came_from.clear()
        self.g_score.clear()
        self.f_score.clear()

        for node_id in graph.nodes:
            self.g_score[node_id] = float("inf")
            self.f_score[node_id] = float("inf")

        self.g_score[start_id] = 0
        self.f_score[start_id] = 0

        heapq.heappush(self.open_set, (0, start_id))

        while self.open_set:
            _, current = heapq.heappop(self.open_set)

            if current == goal_id:
                return self.reconstruct_path(current, graph)

            current_node = graph.nodes[current]

            for neighbor_id in current_node.neighbors:
                neighbor_node = graph.nodes[neighbor_id]

                tentative_g = (
                    self.g_score[current]
                    + self.calculate_weight(current_node, neighbor_node)
                )

                if tentative_g < self.g_score[neighbor_id]:
                    self.came_from[neighbor_id] = current
                    self.g_score[neighbor_id] = tentative_g
                    self.f_score[neighbor_id] = (
                        tentative_g + self.heuristic(neighbor_node, graph.nodes[goal_id])
                    )

                    heapq.heappush(
                        self.open_set, (self.f_score[neighbor_id], neighbor_id)
                    )

        return []  # yol bulunamazsa
