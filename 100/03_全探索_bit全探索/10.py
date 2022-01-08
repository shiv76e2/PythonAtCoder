#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A
n_un = int(input())
un = tuple(map(int, input().split()))
set_tot_numbers = {0}

for bit in range(2 ** n_un):
    tot = 0
    for i in range(n_un):
        if (bit >> i) & 1:
            tot += un[i]
    set_tot_numbers.add(tot)

n_an = int(input())
an = tuple(map(int, input().split()))

for ans_num in an:
    if ans_num in set_tot_numbers:
        print("yes")
    else:
        print("no")
