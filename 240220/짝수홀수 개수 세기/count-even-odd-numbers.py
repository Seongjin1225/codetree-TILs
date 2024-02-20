n = int(input())

cnt = 0
cn = 0

for i in range(n):
    num = int(input())
    if num == 0:
        break

    elif num%2==0:
        cnt += 1
    elif num%2 !=0 :
        cn += 1

print(cnt)
print(cn)