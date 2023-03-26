import itertools

n_ipt = int(input())
li_ipt = list(map(int, input().split()))
acc_li = list(itertools.accumulate(li_ipt))
ans_li = []

#連続したK+1個の区間を探索
for k in range(0, n_ipt):
    max_val = 0
    lst_index = n_ipt-k
    for i in range(0, lst_index):
        cut_i = i-1
        end_i = i+k
        end_num = acc_li[end_i]
        cut_num = acc_li[cut_i] if cut_i >= 0 else 0
        num = end_num - cut_num
        if num > max_val:
            max_val = num
    ans_li.append(max_val)

for num in ans_li:
    print(num)


