#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja

# N: 頂点数
N = int(input())
# G[v]: 頂点vに隣接する頂点lists
G = {}

for _ in range(N):
    li = list(map(lambda a: int(a) - 1, input().split()))
    v = li[0]
    n = li[1] + 1
    if n != 0:
        G[v] = li[2: n + 2]
    else:
        G[v] = []

from collections import deque
dist = [-1] * N
que = deque([0])
dist[0] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)

for i in range(N):
    print(i + 1, dist[i])
