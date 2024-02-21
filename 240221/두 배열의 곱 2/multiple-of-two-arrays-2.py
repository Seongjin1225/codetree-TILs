arr = [list(map(int,input().split())) for _ in range(4)]
_ = input()
arr_2 = [list(map(int,input().split())) for _ in range(4)]

new_arr = []
for i in range(4):
    for j in range(2):
        print(arr[i][j] * arr_2[i][j],end=' ')
    print()