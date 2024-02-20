n = int(input())
num = tuple(map(int,input().split()))

lst = []
for elem in num:
    if (elem%5==0) or (elem%7==0):
        continue
    else:
        lst.append(elem)

print(sum(lst))
print(f'{sum(lst)/len(lst):.1f}')