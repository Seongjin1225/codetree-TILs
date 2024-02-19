n = int(input())

i = 1
while True:
    if n*i > 200:
        break
    print(n*i, end=' ')
    if (n*i)%10 == 0:
        break
    i += 1