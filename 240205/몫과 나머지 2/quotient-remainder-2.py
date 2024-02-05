x,y = tuple(map(int,input().split()))
target = x//y
left = x%y
print(f'{target}---{left}')