n,m = tuple(map(int,input().split()))

if m == 1:
    for i in range(n):
        if i <= n//2:
            print('*'*(i+1),end='')
            print()
        else:
            print('*'*(n-i),end='')
            print()
elif m == 2:
    for i in range(n):
        if i <= n//2:
            print(' '*(n//2-i),end='')
            print('*'*(i+1),end='')
            print()
        else:
            print(' '*(i-n//2),end='')
            print('*'*(n-i),end='')
            print()
elif m == 3:
    num = n//2
    for i in range(num,0,-1):
        print(' '* (num-i) + '*' * (i * 2 + 1))
    for i in range(num+1):
        print(' '* (num-i) + '*' * (i * 2 + 1))  

else:
    for i in range(n):
        if i <= n // 2:
            print(" " * i + "*" * (n -(n // 2) - i))
        else:
            print(" " * (n // 2) + "*" * (i-n//2+1))