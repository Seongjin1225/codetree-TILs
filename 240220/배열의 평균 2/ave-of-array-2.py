arr = [list(map(int,input().split())) for _ in range(3)]

row_avg = []
col_avg = []
total_avg = 0

for i in range(3):
    row_val = 0
    col_val = 0
    for j in range(3):
        row_val += arr[i][j]
        col_val += arr[j][i]
        total_avg += arr[i][j]
    row_avg.append(f'{row_val/3:.1f}')
    col_avg.append(f'{col_val/3:.1f}')

for elem in row_avg:
    print(elem,end=' ')
print()
for elem in col_avg:
    print(elem,end=' ')
print()
print(f'{total_avg/9:.1f}')