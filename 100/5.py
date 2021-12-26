#https://atcoder.jp/contests/abc095/tasks/arc096_a

A, B, C, X, Y = list(map(int, input().split()))


# 別々に買う
ans = X * A + Y * B

if X <= Y:
    # X*2枚Cを買う
    ans = min(ans, C * X*2 + B * (Y - X))
    # Y*2枚Cを買う
    ans = min(ans, C*Y*2)


if Y <= X:
    # Y*2枚をCを買う
    ans = min(ans, C * Y*2 + A * (X - Y))
    # X*2枚Cを買う
    ans = min(ans, C*X*2)

print(ans)





