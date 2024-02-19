n = int(input())

i = 1
while True:
    print(n*i, end=' ')
    if n*i > 200:
        break
    if (n*i)%10 == 0:
        break
    i += 1