#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
from heapq import heappush, heappop

INF = 10 ** 10


def dijkstra(N, G, s):
    dist = [INF] * N
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    for i in range(V):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])


# V: 頂点数
V, E, r = map(int, input().split())
# g[v] = {(w, cost)}:
# 頂点vから遷移可能な頂点(w)とそのコスト(cost)
g = [set() for _ in range(V)]
for i in range(E):
    v, w, c = list(map(int, input().split()))
    g[v].add((w, c))
# r: 始点の頂点


dijkstra(V, g, r)
