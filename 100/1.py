#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja

while True:

    li = list(map(int, input().split()))
    n = li[0]
    x = li[1]

    if x == 0 and n == 0:
        break

    ans = 0
    for num1 in range(1, n+1):
        for num2 in range(num1+1, n+1):
            for num3 in range(num2+1, n+1):
                if (num1 + num2 + num3) == x:
                    ans += 1

    print(ans)


