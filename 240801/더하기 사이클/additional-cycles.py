n = int(input())
original_n = n
cnt = 0

while True:
    cnt += 1
    if n < 10:
        n = n * 10 + n
    else:
        tens = n // 10
        ones = n % 10
        n = ones * 10 + (tens + ones) % 10

    if n == original_n:
        break

print(cnt)