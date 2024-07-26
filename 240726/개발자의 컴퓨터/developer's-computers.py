n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

max_val = max(max(arr))
new_arr = [0]*(max_val+1)

for i in arr:
    start,end,plus = i
    for j in range(start,end+1):
        new_arr[j] += plus

print(max(new_arr))