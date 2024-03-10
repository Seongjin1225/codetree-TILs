n = int(input())
arr = list(map(int,input().split()))

max_val = 999
min_num = 0
lst = []

for elem in arr:
    if elem < 100:
        val = abs(elem-100)
        if val < max_val:
            val = max_val
            min_num = elem
    else:
        lst.append(elem)
        if len(lst) == 0:
            num_2 = -1
        else:
            num_2 = min(lst)

print(min_num, num_2)