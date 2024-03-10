arr = list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] == -999:
        arr = arr[:i]
print(max(arr), min(arr))