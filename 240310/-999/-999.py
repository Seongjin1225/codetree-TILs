arr = list(map(int,input().split()))

if -999 in arr:
    i = arr.index(-999)
    arr = arr[:i]
print(max(arr), min(arr))