n, m, k = tuple(map(int, input().split()))
arr = [input() for _ in range(n)]

for row in arr:
    expanded_row = ''.join([char * k for char in row]) 
    for j in range(k):
        print(expanded_row)