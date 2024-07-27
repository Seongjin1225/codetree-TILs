# n = 3
# full = []  # 각 물병의 최대용량
# now = []   # 현재 들어있는 용량
# cnt = 0

# for _ in range(n):
#     x,y = list(map(int,input().split()))
#     full.append(x)
#     now.append(y)

# for _ in range(100//3 + 1):
#     for i in range(len(now)):
#         if i != 2 & :
#             now[i+1] += now[i]
#             now[i] = 0
#             if now[i+1] > full[i+1]:
#                 temp = now[i+1] - full[i+1]
#                 now[i+1] = full[i+1]
#                 now[i] = tmp
#             cnt += 1
#         else:
#             now[0] += now[i]
#             now[i] = 0
#             if now[0] > full[0]:
#                 tmp = now[0] - full[0]
#                 now[0] = full[0]
#                 now[2] = tmp
#             cnt += 1
#         if cnt == 100:
#             break

# for elem in now:
#     print(elem)

n = 3
full = []  # 각 물병의 최대용량
now = []   # 현재 들어있는 용량
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    full.append(x)
    now.append(y)

# 물병의 용량을 순환적으로 이동
for _ in range(100//3 + 1):
    # 1번 물병 -> 2번 물병
    now[1] += now[0]
    if now[1] > full[1]:
        now[0] = now[1] - full[1]
        now[1] = full[1]
    else:
        now[0] = 0
    cnt+=1
    if cnt == 100:
        break
    # 2번 물병 -> 3번 물병
    now[2] += now[1]
    if now[2] > full[2]:
        now[1] = now[2] - full[2]
        now[2] = full[2]
    else:
        now[1] = 0
    cnt += 1

    # 3번 물병 -> 1번 물병
    now[0] += now[2]
    if now[0] > full[0]:
        now[2] = now[0] - full[0]
        now[0] = full[0]
    else:
        now[2] = 0
    cnt +=1 

for elem in now:
    print(elem)