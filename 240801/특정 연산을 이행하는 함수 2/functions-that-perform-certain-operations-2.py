import math
# ceil - 올림
# round(n,자리수) - 반올림
# floor - 내림
num = list(map(float,input().split()))

def calc(num):
    max_val = max(num)
    min_val = min(num)
    for elem in num:
        if min_val <= elem and max_val >= elem:
            mid_val = elem
    for i in range(3):
        if num[i] == min_val:
            print(math.floor(num[i]),end=' ')
        elif num[i] == max_val:
            print(math.ceil(num[i]),end=' ')
        else:
            print(int(round(num[i],0)),end=' ')

calc(num)