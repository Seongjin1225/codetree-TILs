# 1 -> i 번째 원소의 상태를 x로 변경합니다.
# 2 -> i 번째부터 j 번째까지의 원소의 상태를 0은 1로, 1은 0으로 변경합니다.
# 3 -> i 번째부터 j 번째까지의 원소를 0으로 변경합니다.
# 4 -> i 번째부터 j 번째까지의 원소를 1로 변경합니다.

n,m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

for _ in range(m):
    a,b,c = tuple(map(int,input().split()))

    if a == 1:
        arr[b-1] = c
    elif a == 2:
        for i in range(b-1,c):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    elif a == 3:
        for i in range(b-1,c):
            arr[i] = 0
    elif a == 4:
        for i in range(b-1,c):
            arr[i] = 1
for elem in arr:
    print(elem, end=' ')