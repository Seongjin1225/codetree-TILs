# 3,5,8번째는 더하고 
# 7번째는 빼기

n = int(input())
arr = list(map(int,input().split()))
val = 0
val_2 = 0

for i in range(len(arr)):
    if i == 2 or i == 4 or i == 7:
        val += arr[i]
    if i == 6:
        val_2 += arr[i]

print(val-val_2)