import time

class temelAlgoritma:
    def __init__(self, graph):
        self.graph = graph

    def sure_olc(self, t1):
        return round(time.time() - t1, 6)
