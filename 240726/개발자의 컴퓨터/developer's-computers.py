# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))

# max_val = max(max(arr))
# new_arr = [0]*(max_val+1)

# for i in arr:
#     start,end,plus = i
#     for j in range(start,end+1):
#         new_arr[j] += plus

# print(max(new_arr))
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 각 리스트의 두 번째 요소들 중 최대값을 찾아서 max_val을 설정
max_val = max([end for _, end, _ in arr])
new_arr = [0] * (max_val + 1)

for i in arr:
    start, end, plus = i
    for j in range(start, end + 1):
        new_arr[j] += plus

print(max(new_arr))