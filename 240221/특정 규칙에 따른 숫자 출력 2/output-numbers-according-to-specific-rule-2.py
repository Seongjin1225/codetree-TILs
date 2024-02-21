n = int(input())

start = 9
for i in range(n):
    for _ in range(n):
        print(start,end=' ')
        start-=2
        if start < 1:
            start = 9
    print()