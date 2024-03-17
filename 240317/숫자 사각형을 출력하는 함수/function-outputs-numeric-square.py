n = int(input())

def show(num):
    val = 1
    arr = [[0 for _ in range(num)] for _ in range(num)]
    for j in range(n):
        for i in range(n):
            arr[i][j] += val
            val+=1
    return arr

ans = show(n)

for elem in ans:
    for e in elem:
        print(e,end=' ')
    print()