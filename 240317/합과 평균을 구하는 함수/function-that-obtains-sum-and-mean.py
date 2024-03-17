import math 
arr = list(map(float,input().split()))

def calc(lst):
    val = []
    for elem in lst:
        val.append(round(elem))
    ans = sum(val)
    avg = ans/3
    print(f'{ans:.0f}')
    print(f'{avg:.0f}')
    
calc(arr)