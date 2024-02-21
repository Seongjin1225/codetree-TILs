# 행 -> 가로
arr = [list(map(int,input().split())) for _ in range(5)]

sum_val = []

for i in range(5):
    val = 0
    for j in range(4):
        val+=arr[i][j]
    sum_val.append(val)

for elem in sum_val:
    print(elem)