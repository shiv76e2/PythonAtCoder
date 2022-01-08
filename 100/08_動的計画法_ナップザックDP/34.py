# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A

N = int(input())


def fibo(n):
    dp = {0: 1, 1: 1}
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(fibo(N))
