import time
from collections import deque
from algorithms.baseAlgorithm import temelAlgoritma


class BagliBilesenler(temelAlgoritma):
    def calistir(self):
        t1 = time.time()

        ziyaret = set()
        gruplar = []

        # Graph üzerindeki tüm düğümler
        for node_id in self.graph.nodes:
            if node_id not in ziyaret:
                grup = []
                kuyruk = deque([node_id])
                ziyaret.add(node_id)

                while kuyruk:
                    curr_id = kuyruk.popleft()
                    curr_node = self.graph.nodes[curr_id]

                    grup.append(f"{curr_node.name} ({curr_id})")

                    for komsu_id in curr_node.neighbors:
                        if komsu_id not in ziyaret:
                            ziyaret.add(komsu_id)
                            kuyruk.append(komsu_id)

                gruplar.append(grup)

        return {
            "gruplar": gruplar,
            "adet": len(gruplar),
            "sure": self.sure_olc(t1)
        }
