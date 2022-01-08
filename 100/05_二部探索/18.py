#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B

from bisect import bisect_left

n = int(input())
li = list(map(int, input().split()))
input()
list_check = list(map(int, input().split()))

ans = 0
for number in list_check:
    index = bisect_left(li, number)
    if index < n and li[index] == number:
        ans += 1
print(ans)
