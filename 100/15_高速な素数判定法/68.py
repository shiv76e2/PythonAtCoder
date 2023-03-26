#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A&lang=ja

import math

def factorization(n):
    pfs = []
    while n >= 2:
        pf = first_prime(n)
        if pf != n:
            pfs.append(pf)
            n = n / pf
        else:
            pfs.append(n)
            break
    return pfs

def first_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return int(n)


n_ipt = int(input())

print(n_ipt, end=":")
for i in factorization(n_ipt):
    print(" ", end="")
    print(int(i), end="")
print()
