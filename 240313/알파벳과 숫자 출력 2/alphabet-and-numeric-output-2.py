n = int(input())
alp = 65
num = 0
idx = 0

for i in range(n,-1,-1):
    for j in range(i):
        print(chr(alp),end=' ')
        alp += 1
        if alp > 90:
            alp=65
    if i != n:
        if i != 0:
            for k in range(idx):
                print(num,end=' ')
                num+=1
                if num>9:
                    num=0
        else:
            for _ in range(n):
                print(num,end=' ')
                num+=1
                if num>9:
                    num=0
    idx+=1
    print()