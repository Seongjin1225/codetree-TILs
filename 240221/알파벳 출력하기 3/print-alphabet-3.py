# 65 ~ 90까지

n = int(input())

start = 65
for i in range(n):
    for j in range(n-i):
        print(chr(start),end='')
        start += 1
        if start > 90:
            start = 65
    print()