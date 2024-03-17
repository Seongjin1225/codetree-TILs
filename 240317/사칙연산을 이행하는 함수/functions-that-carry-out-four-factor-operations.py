x,a,y = input().split()

def calc(a,b,c):
    val = 0
    a = int(a)
    c = int(c)
    if b == '+':
        val = a + c
    elif b == '-':
        val = a-c
    elif b == '*':
        val = a*c
    else:
        val = a//c
    return val

print(f'{x} {a} {y} = {calc(x,a,y)}')