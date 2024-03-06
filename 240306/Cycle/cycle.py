n,p = tuple(map(int,input().split()))

cnt = 0
lst = [n]

start = n
while True:
    val = (start*n)%p
    if val not in lst:
        lst.append(val)
        cnt += 1
    else:
        break
    start = val
    
print(cnt)