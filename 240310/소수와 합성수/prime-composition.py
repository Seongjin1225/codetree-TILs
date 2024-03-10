import math 

n = int(input())

cnt = 0
if n == 1:
    print('one')
else:
    num = math.sqrt(n)
    for i in range(1,int(num)+1):
        if n%i != 0:
            print('prime')
            break
        else:
            cnt += 1
    if cnt > 2:
        print('composition')