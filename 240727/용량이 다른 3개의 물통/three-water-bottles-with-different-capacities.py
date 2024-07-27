n = 3
full = []  # 각 물병의 최대용량
now = []   # 현재 들어있는 용량
cnt = 0

for _ in range(n):
    x,y = list(map(int,input().split()))
    full.append(x)
    now.append(y)

for _ in range(100//3 + 1):
    for i in range(len(now)):
        if i != 2:
            now[i+1] += now[i]
            now[i] = 0
            if now[i+1] > full[i+1]:
                temp = now[i+1] - full[i+1]
                now[i+1] = full[i+1]
                now[i] = tmp
            cnt += 1
        else:
            now[0] += now[i]
            now[i] = 0
            if now[0] > full[0]:
                tmp = now[0] - full[0]
                now[0] = full[0]
                now[2] = tmp
            cnt += 1
        if cnt == 100:
            break

for elem in now:
    print(elem)
    print()