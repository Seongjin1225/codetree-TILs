value = 1
for _ in range(3):
    a = int(input())
    value*=a

arr = [0]*10

for elem in str(value):
    arr[int(elem)]+=1

for elem in arr:
    print(elem)