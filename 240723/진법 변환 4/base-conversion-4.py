num = int(input())
ans = 0
n = len(str(num))
for i in range(n-1,-1,-1):
    ans += (2**(n-i-1))*(int(str(num)[i]))
print(ans)