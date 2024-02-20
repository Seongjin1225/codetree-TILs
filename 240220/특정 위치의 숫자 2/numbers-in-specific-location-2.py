n = int(input())
num = tuple(map(int,input().split()))

sum_val = 0
cnt = 0

for i in range(len(num)):
    if i%2 !=0:
        sum_val+=num[i]
        cnt+=1

print(sum_val,end=' ')
print(f'{sum_val/cnt:.1f}')