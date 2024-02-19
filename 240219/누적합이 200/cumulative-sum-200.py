n = int(input())
num = tuple(map(int,input().split()))

val = 0
cnt = 0

for elem in num:
    val += elem
    cnt += 1
    if val > 200:
        break

avg = val/cnt

print(val)
print(f'{avg:.1f}')