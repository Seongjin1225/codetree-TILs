import math

a,b = list(map(float,input().split()))

def btw(x,y):
    cnt = 0
    x**=(1/2)
    y**=(1/2)
    x = math.trunc(x)
    y = math.trunc(y)
    return y-x

print(abs(btw(a,b)))