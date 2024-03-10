import math 

n = int(input())

cnt = 0
if n == 1:
    print('one')
else:
    num = math.sqrt(n)
    for i in range(2,int(num)+1):
        if n%i == 0:
            print('composition')
            break
        else:
            print('prime')
            break