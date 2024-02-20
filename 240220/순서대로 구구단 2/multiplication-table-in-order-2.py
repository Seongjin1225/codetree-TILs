a,b = tuple(map(int,input().split()))

if a > b:
    for i in range(a,b-1,-1):
        for j in range(1,10):
            if j%3==0:
                print(f'{i} * {j} = {i*j}',end='\n')
            else:
                print(f'{i} * {j} = {i*j}',end='  ')
        print()
else:
    for i in range(a,b+1):
        for j in range(1,10):
            if j%3==0:
                print(f'{i} * {j} = {i*j}',end='\n')
            else:
                print(f'{i} * {j} = {i*j}',end='  ')
        print()