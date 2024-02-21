n = int(input())

for i in range(n):
    print(' ',end='')
    for j in range(1, n-i+1):
        print(j,end=' ')
    print()