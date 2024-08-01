n = int(input())


def calc(num):
    val = 0
    if num%2 == 0:
        for i in range(num,101):
            if i%2==0:
                val += i
    else:
        for i in range(num,101):
            if i%2 !=0:
                val +=i
    return val

print(calc(n))