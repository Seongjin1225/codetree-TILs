n = int(input())

def calc_sum(num):
    val = 0
    for i in range(10,num+1):
        val += i
    return val

print(calc_sum(n))