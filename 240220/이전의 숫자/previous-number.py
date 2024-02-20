n = int(input())
num = tuple(map(int,input().split()))

for i in range(len(num)):
    if num[i] == 0:
        new_num = num[i-5:i]
    
print(sum(new_num))