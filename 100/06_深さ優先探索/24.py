#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B

n = int(input())
dic_edge_node = {}
for _ in range(n):
    li = list(map(int, input().split()))
    node = li[0]
    edge_count = li[1]
    edge_list = []
    for i in range(2, edge_count + 2):
        edge_list.append(li[i])
    dic_edge_node[node] = edge_list

# edgeを渡されて、隣接しているedgeを再帰的に探索し、タイムスタンプを立てる。
dic_edge_timestamp = {}
time = 0
visited_edge = set()


def dfs(edge):
    global time
    global visited_edge
    if edge in visited_edge:
        return
    time += 1
    visited_edge.add(edge)
    dic_edge_timestamp[edge] = [time]
    for e in dic_edge_node[edge]:
        dfs(e)
    time += 1
    dic_edge_timestamp[edge] += [time]


while len(visited_edge) < n:
    # 訪れてない頂点をdfs
    for e in dic_edge_node.keys():
        for edge in dic_edge_node[e]:
            dfs(e)

sorted_timestamp = sorted(dic_edge_timestamp.items(), key=lambda x: x[0])

for item in sorted_timestamp:
    print(item[0], item[1][0], item[1][1])
