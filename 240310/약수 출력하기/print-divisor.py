import math 
 
n = int(input())
num = int(math.sqrt(n))
ans = []

for i in range(1,num+1):
    if n%i == 0:
        ans.append(i)
        if n//i not in ans:
            ans.append(n//i)

for elem in (sorted(ans)):
    print(elem,end=' ')