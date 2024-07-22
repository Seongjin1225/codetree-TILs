n = int(input())
arr = []
for in range(n):
    arr.append(list(map(int,input().split())))
print(sum(arr[1]))
# def extend(arr):
#     n = len(arr)

#     new_arr = [[0]*(n+1) for _ in range(n+1)]

#     for i in range(n):
#         sum_1 = sum(arr[i])