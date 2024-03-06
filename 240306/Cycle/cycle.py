n,p = tuple(map(int,input().split()))

lst = []

start = n
while True:
    val = (start*n)%p
    if val not in lst:
        lst.append(val)
    else:
        print(len(lst)-lst.index(val))
        break
    start = val