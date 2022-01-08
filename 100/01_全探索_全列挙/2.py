#https://atcoder.jp/contests/abc106/tasks/abc106_b

N = int(input())


def is_div8(n):
    div_cnt = 0
    for i in range(1, n + 1):
        if num % i == 0:
            div_cnt += 1

    return div_cnt == 8


ans = 0
for num in range(1, N + 1):
    if num % 2 == 0: continue
    if is_div8(num):
        ans += 1

print(ans)
