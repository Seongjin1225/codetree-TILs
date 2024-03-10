n,m = tuple(map(int,input().split()))
arr = [[0 for _ in range(m)] for _ in range(n)]

num = 0
for j in range(m):
    for i in range(n):
        num += 1
        arr[i][j] += num
        
for elem in arr:
    for e in elem:
        print(e, end=' ')
    print()