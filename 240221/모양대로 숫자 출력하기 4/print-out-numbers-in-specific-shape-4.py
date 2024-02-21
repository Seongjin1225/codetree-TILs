n = int(input())

start = 2
for i in range(n):
    print('  '*i,end='')
    for j in range(n-i):
        print(start, end=' ')
        start += 2
        if start > 8:
            start = 2
    print()