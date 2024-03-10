n = int(input())
arr = [['' for _ in range(n)] for _ in range(n)]

num = 65 # ASCII 코드 시작 

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        arr[j][i] += chr(num)
        num += 1

for elem in arr:
    for e in elem:
        print(e,end=' ')
    print()