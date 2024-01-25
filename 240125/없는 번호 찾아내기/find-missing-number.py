arr = []
for _ in range(28):
    arr.append(int(input()))
ans = []

for i in range(1,31):
    if i in arr:
        continue
    else:
        ans.append(i)

sorted(ans)
print(ans[0])
print(ans[1])