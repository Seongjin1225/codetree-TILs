from math import prod

num = list(map(int,input().split()))
arr = []

for i in range(len(num)):
    for j in range(i,len(num)):
        arr.append(num[i]*num[j])
arr.append(prod(num))

ans = []
for elem in arr:
    if elem%2 != 0:
        ans.append(elem)
print(max(ans))