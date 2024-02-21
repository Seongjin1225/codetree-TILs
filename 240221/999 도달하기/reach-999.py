n = int(input())

arr = [1,n]

i = 0
while True:
    if i == 0:
        print(1,end=' ')
    if i == 1:
        print(n,end=' ')
    if i >= 2:
        num = arr[i-2]+arr[i-1]
        print(num,end=' ')
        arr.append(num)
        if num > 999:
            break
    i += 1