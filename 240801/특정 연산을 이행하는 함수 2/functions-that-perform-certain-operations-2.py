import math
# ceil - 올림
# round(n,자리수) - 반올림
# floor - 내림
# 큰거, 작은거, 중간 순
num = list(map(float,input().split()))
new_num = sorted(num)

def calc(num):
    print(math.ceil(num[2]),end=' ')
    print(math.floor(num[0]),end=' ')
    print(int(round(num[1],0)))

calc(new_num)