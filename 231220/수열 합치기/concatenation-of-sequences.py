n,m = tuple(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

new_arr = a + b
new_arr = sorted(new_arr)
for elem in new_arr:
    print(elem, end=' ')