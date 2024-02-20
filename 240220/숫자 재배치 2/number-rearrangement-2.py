n = int(input())
num = list(map(int,input().split()))

new_num = num[::-1]
for elem in new_num:
    print(elem, end=' ')