n = int(input())
num = tuple(map(int,input().split()))

arr = []
for elem in num:
    if elem%7 == 0:
        arr.append(elem)

print(len(arr),end=' ')
print(sum(arr),end=' ')
print(f'{sum(arr)/len(arr):.1f}')