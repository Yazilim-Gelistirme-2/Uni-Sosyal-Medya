class WelshPowell:

    @staticmethod
    def color_graph(graph):

        nodes_sorted = sorted(
            graph.nodes.values(),
            key=lambda node: len(node.neighbors),
            reverse=True
        )

        color_of = {}
        current_color = 1

        for node in nodes_sorted:
            if node.id in color_of:
                continue


            color_of[node.id] = current_color

            for other in nodes_sorted:
                if other.id in color_of:
                    continue


                conflict = False
                for colored_node_id, color in color_of.items():
                    if color == current_color:
                        if colored_node_id in other.neighbors:
                            conflict = True
                            break

                if not conflict:
                    color_of[other.id] = current_color

            current_color += 1

        return color_of
