n = int(input())
strin,num = 65,1
idx = 1
for i in range(n,0,-1):
    for j in range(i):
        print(chr(strin),end=' ')
        strin += 1
        if strin > 90:
            strin = 65  
    for k in range(idx):
        print(num,end=' ')
        num+=1
        if num > 9:
            num = 1
    idx+=1
    print()