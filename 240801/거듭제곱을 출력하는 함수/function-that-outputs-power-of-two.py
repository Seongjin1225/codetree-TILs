num = list(map(int,input().split()))
a,b = num

def double(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a*double(a,b-1) 

print(double(a,b))