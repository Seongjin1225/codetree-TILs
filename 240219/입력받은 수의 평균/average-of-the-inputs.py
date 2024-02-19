n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

avg = sum(num)/len(num)
ans = f'{avg:.1f}'

if float(ans) >= 70:
    print(ans)
else:
    print(ans)
    print('fail')