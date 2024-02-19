x,y = tuple(map(int,input().split()))

num = []

if x > y:
    for i in range(y,x+1):
        if i%5 !=0:
            num.append(i)
else:
    for i in range(x,y+1):
        if i%5 !=0:
            num.append(i)

sum_val = sum(num)
avg = sum_val/len(num)

print(sum_val,end=' ')
print(f'{avg:.1f}')