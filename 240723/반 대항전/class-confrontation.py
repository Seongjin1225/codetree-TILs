n = int(input())

arr = []
ans = []
alp = 65
for _ in range(4):
    arr.append(list(input().split()))

val = 0
for i in range(len(arr)):
    for j in range(1,n+1):
        val += int(arr[i][j])
    ans.append([chr(alp),val])
    alp+=1
    val = 0

for elem in ans:
    print(elem[0],"-",elem[1])

max_value = max(ans, key=lambda x: x[1])
print('Class {} is winner!'.format(max_value[0]))