n = int(input())

for i in range(n):
    print('*'*((n-i)*2))
for j in range(n-2,-1,-1):
    print('*'*((n-j)*2))