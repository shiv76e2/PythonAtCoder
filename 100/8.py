#https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

n = int(input())
a_list = []
b_list = []

total_dist_ab = 0
for _ in range(n):
    a, b = map(int, input().split())
    total_dist_ab += abs(a - b)
    a_list += [a]
    b_list += [b]

from statistics import median

total_dist_a = 0
a_med = median(a_list)
for i in a_list:
    total_dist_a += abs(a_med - i)

total_dist_b = 0
b_med = median(b_list)
for i in b_list:
    total_dist_b += abs(b_med - i)

print(int(total_dist_ab + total_dist_a + total_dist_b))
