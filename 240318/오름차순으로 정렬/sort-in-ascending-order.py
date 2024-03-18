n = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=False)

for elem in arr:
    print(elem,end=' ')