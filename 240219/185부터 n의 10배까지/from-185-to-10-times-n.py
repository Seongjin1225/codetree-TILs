n = int(input())

sum_val = 0
cnt = 0
for i in range(185, n*10+1):
    sum_val += i
    cnt += 1

avg = sum_val/cnt
avg = f'{avg:.1f}'

print(sum_val,end=' ')
print(avg)