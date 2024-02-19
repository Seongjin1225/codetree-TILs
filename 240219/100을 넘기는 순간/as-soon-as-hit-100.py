n = int(input())
num = list(map(int,input().split()))

val = 0
for i in range(len(num)):
    val += num[i]
print(val)
print(f'{val/len(num):.1f}')