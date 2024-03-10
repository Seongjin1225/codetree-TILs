# 65 ~ 90

n = int(input())
arr = [['' for _ in range(n)]for _ in range(n)]
num = 65

for i in range(n):
    if i%2 == 0:
        for j in range(n):
            arr[j][i] += chr(num)
            num += 1
            if num > 90:
                num = 65
    else:
        for j in range(n-1,-1,-1):
            arr[j][i] += chr(num)
            num += 1
            if num > 90:
                num = 65
            

for elem in arr:
    for e in elem:
        print(e,end=' ')
    print()