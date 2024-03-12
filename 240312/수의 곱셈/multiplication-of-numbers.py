from math import prod

num = list(map(int,input().split()))
arr = []

for i in range(len(num)):
    for j in range(i+1,len(num)):
        arr.append(num[i]*num[j])
arr.append(prod(num))

num+=arr

ans = []
for elem in num:
    if elem%2 != 0:
        ans.append(elem)
    
if len(ans) == 0:
    print(max(arr))
else:
    print(max(ans))