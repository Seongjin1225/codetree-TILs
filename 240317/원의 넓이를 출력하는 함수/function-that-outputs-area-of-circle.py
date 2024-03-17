# 원 넓이 = 반지름 * 반지름 * 3.14

n = int(input())

def one(num):
    val = n*n*3.14
    return f'{val:.2f}'

print(one(n))