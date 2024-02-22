# (i,j) = (i-1, j-1) + (i-1,j)

n = int(input())
arr = []
for i in range(n):
    start = 2
    lst = []
    for j in range(i+1):
        if j == 0 or j == i:
            lst.append(start)
        else:
            lst.append((arr[i-1][j-1]) + (arr[i-1][j]))
    arr.append(lst)

for elem in arr:
    for el in elem:
        print(el,end=' ')
    print()