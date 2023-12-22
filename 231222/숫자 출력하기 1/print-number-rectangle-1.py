n,m = tuple(map(int,input().split()))

arr = []

k= 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(k)
        k += 1
    arr.append(row)
# print(arr)

for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()