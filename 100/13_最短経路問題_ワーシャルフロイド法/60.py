# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja


V, E = map(int, input().split())
INF = 10 ** 20

cost = [[INF for i in range(V)] for j in range(V)]
for i in range(V):
    cost[i][i] = 0
for _ in range(E):
    s, t, d = map(int, input().split())
    cost[s][t] = d

# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
for k in range(V):
    for i in range(V):
        for j in range(V):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
                if cost[i][i] < 0:
                    print("NEGATIVE CYCLE")
                    exit()

for i in range(V):
    for j in range(V):
        if cost[i][j] == INF:
            if j == V - 1:
                print("INF", end="")
            else:
                print("INF", end=" ")
        else:
            if j == V - 1:
                print(cost[i][j], end="")
            else:
                print(cost[i][j], end=" ")
    print()
