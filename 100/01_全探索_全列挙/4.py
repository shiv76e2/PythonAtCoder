#https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c


#テーブル生成
N, M = list(map(int, input().split()))
table = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    li = list(map(int, input().split()))
    for j in range(M):
        table[i][j] = li[j]


#全探索
ans = 0
tmp_max_point = 0

for i_song1 in range(M):
    for i_song2 in range(i_song1+1, M):
        tmp_max_point = 0
        for i_man in range(N):
            tmp_max_point += max(table[i_man][i_song1], table[i_man][i_song2])
        if tmp_max_point > ans:
            ans = tmp_max_point

print(ans)

