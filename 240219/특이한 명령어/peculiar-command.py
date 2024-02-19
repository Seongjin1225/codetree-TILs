n = int(input())

for i in range(n):
    a,b,order = tuple(input().split())
    a,b = int(a), int(b)

    if order == 's':
        print(a*b)
    elif order == 't':
        print((1/2)*(a*b))
    else:
        continue