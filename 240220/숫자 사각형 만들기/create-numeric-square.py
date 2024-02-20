n = int(input())

start = 9

for i in range(1,n+1):
    for _ in range(1,n+1):
        if start <+ 1:
            print(1,end=' ')
        else:
            print(start, end=' ')
        start-=1
    start = 9-i
    print(end='\n')