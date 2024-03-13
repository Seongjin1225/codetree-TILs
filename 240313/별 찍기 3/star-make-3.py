n = int(input())

for i in range(n):
    if i <= n//2:
        print(' '*i,end='')
        print('*'*(2*i+1),end='')
        print()
    else:
        print(' '*(n-i-1),end='')
        print('*'*(2*(n-i-1)+1),end='')
        print()