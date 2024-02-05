a,b,c = tuple(map(int,input().split()))

if b > a and b > c:
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b==c:
    print(1)
else:
    print(0)