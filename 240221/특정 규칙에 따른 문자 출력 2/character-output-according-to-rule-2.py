n = int(input())

for i in range(1, n + 1):
    print('@ ' * i)

for j in range(n - 1):
    print(' ' * (2 * (j + 1)), end='')  
    print('@ ' * (n - 1 - j))