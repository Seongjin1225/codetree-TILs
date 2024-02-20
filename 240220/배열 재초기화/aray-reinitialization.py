# 행 - 가로, 열 - 세로
# 인덱스는 0부터 시작이므로
# 짝수 행 1로, 홀수 열 2로

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i%2 == 0:
            arr[i][j] = 1
        if j%2 != 0:
            arr[i][j] = 2

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()