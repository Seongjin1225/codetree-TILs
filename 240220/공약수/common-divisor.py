n = int(input())
num = tuple(map(int,input().split()))

if n == 2:
    a,b = num
    for i in range(1,a+1):
        if(a%i) == 0 and (b%i)==0:
            print(i)

else:
    a,b,c = num
    for i in range(1,a+1):
        if a%i == 0 & b%i ==0 & c%i ==0:
            print(i)