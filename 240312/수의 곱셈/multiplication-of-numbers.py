from math import prod

num = list(map(int,input().split()))
arr = []

for i in range(len(num)):
    for j in range(len(num)):
        arr.append(num[i]*num[j])
arr.append(prod(num))

print(max(arr))