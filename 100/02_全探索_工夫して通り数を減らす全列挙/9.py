#https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d

def TI(): return tuple(map(int, input().split()))


n = int(input())
xy = [TI() for _ in range(n)]
vector_xy = [(0, 0)]
point_start_x, point_start_y = xy[0]
for i in range(1, n):
    x, y = xy[i]
    vectorx = x - point_start_x
    vectory = y - point_start_y
    vector_xy.append((vectorx, vectory))


n = int(input())
set_xy_stars = set([TI() for _ in range(n)])
for point in set_xy_stars:
    x, y = point
    flg = True
    for vector in vector_xy:
        vectorx, vectory = vector
        if (x + vectorx, y + vectory) not in set_xy_stars:
            flg = False
    if flg:
        print(x - point_start_x, y - point_start_y)
        break



