# n -> 별 모양 크기
# m -> 별 모양 종류

n,m = tuple(map(int,input().split()))

if m == 1:
    for i in range(1,n+1):
        print('*'*i)
    print()
elif m == 2:
    for i in range(n,0,-1):
        print('*'*i)
    print()
else:
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        print('*'*((2*i)-1),end='')
        print(''*(n-i),end='')
        print()