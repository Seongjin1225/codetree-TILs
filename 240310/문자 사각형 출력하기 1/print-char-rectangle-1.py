n = int(input())
arr = [['' for _ in range(n)] for _ in range(n)]

num = 65 # ASCII 코드 시작 
         # 90 = Z이므로 90까지만

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        arr[j][i] += chr(num)
        num += 1
        if num > 90:
            num = 65

for elem in arr:
    for e in elem:
        print(e,end=' ')
    print()