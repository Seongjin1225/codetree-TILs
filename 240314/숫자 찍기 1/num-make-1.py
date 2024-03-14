n,m = tuple(map(int,input().split()))

if m == 1:
    num = 1
    for i in range(n):
        if i%2 == 0:
            for _ in range(i+1):
                print(num,end=' ')
                num+=1
            print()
        else:
            start = num + i
            end = start - i
            for j in range(i + 1):
                print(start, end=' ')
                start -= 1
            num = end + i + 1
            print()
                
elif m == 2:
    num = 0
    for i in range(n, 0, -1):
        for _ in range(n - i):
            print(' ', end=' ')
        for _ in range(2 * i - 1):
            print(num, end=' ')
        print()
        num += 1
else:
    for i in range(n):
        num = 1
        if i <= n//2:
            for _ in range(i+1):
                print(num,end=' ')
                num+=1
            print()
        else:
            for _ in range(n-i):
                print(num,end=' ')
                num+=1
            print()