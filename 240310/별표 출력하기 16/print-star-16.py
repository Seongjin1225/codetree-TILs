# 각 줄 마다 n의 제곱씩 내림차순으로 출력
n = int(input())

for i in range(n):
    print(' '*(n * n - (n - i) * (n - i)),end='')
    print('*'*((n - i) * (n - i)))