import heapq
import time
from temelAlgoritma import temelAlgoritma

class djikstra(temelAlgoritma):
    def calistir(self, baslangic, hedef):
        t1 = time.time()
        
        ids = [n['id'] for n in self.graf['nodes']]
        adj = {n: [] for n in ids}
        for e in self.graf['edges']:
            adj[e['source']].append(e['target'])
            adj[e['target']].append(e['source'])

        mesafeler = {n: float('inf') for n in ids}
        mesafeler[baslangic] = 0
        nereden = {n: None for n in ids}
        pq = [(0, baslangic)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > mesafeler[u]: continue
            if u == hedef: break

            for v in adj[u]:
                if mesafeler[u] + 1 < mesafeler[v]:
                    mesafeler[v] = mesafeler[u] + 1
                    nereden[v] = u
                    heapq.heappush(pq, (mesafeler[v], v))

        yol = []
        curr = hedef
        if mesafeler[hedef] == float('inf'):
            return {"mesaj": "Yol bulunamadı", "sure": self.sure_olc(t1)}

        while curr is not None:
            n = next(x for x in self.graf['nodes'] if x['id'] == curr)
            yol.append(n['name'])
            curr = nereden[curr]
        
        yol.reverse()
        return {"en_kisa_yol": yol, "mesafe": mesafeler[hedef], "sure": self.sure_olc(t1)}
