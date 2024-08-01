num = list(map(int,input().split()))
a = num[0]**num[1]
b = num[1]**num[0]

def calc(a,b):
    if a>b:
        return a-b
    else:
        return b-a
    
print(calc(a,b))