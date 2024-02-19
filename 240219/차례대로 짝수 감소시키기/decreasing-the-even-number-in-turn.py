n = int(input())
num = 1000
i = 1
lst = []

while True:
    if num == 1000:
        break
    else:
        num -= i*2
        lst.append(i*2)
        if num <= n:
            break
        i += 1

sum_val = sum(lst)
print(len(lst), end=' ')
print(sum_val)