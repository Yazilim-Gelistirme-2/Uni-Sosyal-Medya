import time
from src.utils import get_dynamic_weight

class AStarAlgorithm:
    @staticmethod
    def run(graph, start_id, goal_id):
        t1 = time.time()
        
        open_set = {start_id}
        came_from = {}

        g_score = {node: float("inf") for node in graph.nodes}
        g_score[start_id] = 0
        
        f_score = {node: float("inf") for node in graph.nodes}
        
        f_score[start_id] = get_dynamic_weight(graph.nodes[start_id], graph.nodes[goal_id])

        while open_set:
            current = min(open_set, key=lambda n: f_score[n])

            if current == goal_id:
                path = []
                temp_current = current
                while temp_current in came_from:
                    path.append(temp_current)
                    temp_current = came_from[temp_current]
                path.append(start_id)
                path.reverse()
                
                return path, round(g_score[goal_id], 4)

            open_set.remove(current)

            for neighbor in graph.nodes[current].neighbors:
                weight = get_dynamic_weight(graph.nodes[current], graph.nodes[neighbor])
                
                tentative_g_score = g_score[current] + weight
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    
                    h_score = get_dynamic_weight(graph.nodes[neighbor], graph.nodes[goal_id])
                    f_score[neighbor] = g_score[neighbor] + h_score
                    
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return [], float("inf")
