n = int(input())
arr = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    num = i +1 
    for j in range(n):
        if j == 0:
            arr[i][j] += num
        else:
            arr[i][j] += arr[i][j-1]*2

for elem in arr:
    for el in elem:
        print(el,end=' ')
    print()