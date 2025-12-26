from src.utils import get_dynamic_weight


class AStarAlgorithm:
    @staticmethod
    def run(graph, start_id, goal_id):
        open_set = {start_id}
        came_from = {}

        # Gerçek maliyet tablosu
        g_score = {node: float("inf") for node in graph.nodes}
        g_score[start_id] = 0

        while open_set:
            current = min(open_set, key=lambda n: g_score[n])

            if current == goal_id:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start_id)
                path.reverse()
                return path, g_score[goal_id]

            open_set.remove(current)

            for neighbor in graph.nodes[current].neighbors:
                weight = get_dynamic_weight(graph.nodes[current], graph.nodes[neighbor])
                tentative = g_score[current] + weight
                if tentative < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative
                    open_set.add(neighbor)

        return [], float("inf")