n = int(input())
num = tuple(map(int,input().split()))

five = 0
seven = 0
for elem in num:
    if elem%5==0:
        five+=1
    if elem%7==0:
        seven+=1

print(five)
print(seven)