#https://atcoder.jp/contests/abc122/tasks/abc122_b

li = list(input())
acgt = ["A", "C", "G", "T"]

maxsize_str = 0
size_tmp = 0
for c in li:
    if c in acgt:
        size_tmp += 1
        if size_tmp > maxsize_str: maxsize_str = size_tmp
    else:
        size_tmp = 0

print(maxsize_str)