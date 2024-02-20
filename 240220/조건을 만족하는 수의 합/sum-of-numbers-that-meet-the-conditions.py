n = int(input())

sum_val = 0

for i in range(n,501):
    if i%2 == 0:
        sum_val += i

print(sum_val)