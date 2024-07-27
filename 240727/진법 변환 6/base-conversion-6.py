a,n,b = input().split()
tmp = 0
leng = len(n)
ans = []

# n을 10진수로 변환
if n.isalpha():
    num = ord(n)-87
    for i in range(leng-1,-1,-1):
        tmp += int(num[i])*(2**(leng-i-1))
else:
    for i in range(leng-1,-1,-1):
        tmp += int(n[i])*(2**(leng-i-1))

# 10진수를 b진수로 변환
while True:
    if tmp < int(b):
        ans.append(tmp)
        break
    ans.append(tmp%int(b))
    tmp //=int(b)

ans.reverse()
for elem in ans:
    print(elem,end='')