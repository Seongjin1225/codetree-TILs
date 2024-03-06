a,n = input().split()
n = int(n)

for _ in range(n):
    num = int(input())
    if num > len(a):
        continue
    else:
     val = a[:num-1] + a[num:]
     print(val)
     a = val