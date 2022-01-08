#https://atcoder.jp/contests/abc145/tasks/abc145_c
n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))


import itertools
import math

tot_dist = 0
for pd_li in itertools.permutations(li):
    x, y = pd_li[0]
    for i in range(n):
        next_x, next_y = pd_li[i]
        tot_dist += math.sqrt((next_x - x) ** 2 + (next_y - y) ** 2)
print(tot_dist / math.factorial(n))
