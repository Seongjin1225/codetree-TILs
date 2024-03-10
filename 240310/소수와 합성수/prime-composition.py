import math 

n = int(input())

cnt = 0
if n == 1:
    print('one')
else:
    is_prime = True
    num = math.sqrt(n)
    for i in range(2,int(num)+1):
        if n%i == 0:
            is_prime = False
            break
    if is_prime:
        print('prime')
    else:
        print('composition')