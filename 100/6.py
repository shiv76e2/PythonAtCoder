#https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

n = int(input())
li = list(map(int, list(input())))
# 各数字が左から何番目にあるか
list2 = [[] for i in range(10)]
for i, x in enumerate(li):
    list2[x] += [i]


# 引数以上のlist内の最小値を取得
def fetch_index(idx_list, num):
    for item in idx_list:
        if item > num:
            return item
    return 10**30


ans = 0
for pass_1 in range(10):
    # indexを取得
    i = fetch_index(list2[pass_1], -1)
    if i > 10**20:
        continue
    i_1 = i
    for pass_2 in range(10):
        i = fetch_index(list2[pass_2], i_1)
        if i > 10 ** 20:
            continue
        i_2 = i
        for pass_3 in range(10):
            i = fetch_index(list2[pass_3], i_2)
            if i > 10**20:
                continue
            i_3 = i
            ans += 1


print(ans)
