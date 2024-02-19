n = int(input())

i = 1
while True:
    if n*i > 200:
        break
    if (n*i)%10 == 0:
        break
    print(n*i, end=' ')
    i += 1