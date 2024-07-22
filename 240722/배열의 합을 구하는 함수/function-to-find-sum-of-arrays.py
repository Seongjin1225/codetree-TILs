n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
def extend(arr):
    n = len(arr)

    new_arr = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n):
        sum_1 = sum(arr[i])
        new_arr[i][n] = sum_1   
        for j in range(n):
            new_arr[i][j] = arr[i][j]
            new_arr[n][j] += arr[i][j]
    new_arr[n][n] = sum(new_arr[n][:-1])
    return new_arr

ans = extend(arr)

for elem in ans:
    for e in elem:
        print(e,end=' ')
    print()