n,m = tuple(map(int,input().split()))
start = n*m

for _ in range(n):
    for _ in range(m):
        print(start,end=' ')
        start -= 1
    print(end='\n')