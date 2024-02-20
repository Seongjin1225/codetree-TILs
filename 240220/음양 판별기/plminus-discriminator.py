n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        print('zero')
    elif num > 0:
        print('plus')
    else:
        print('minus')