lst = list(map(int,input().split()))

def change(num):
    val = []
    for elem in num:
        if elem%2 == 0:
            val.append(elem//2)
        else:
            val.append(elem*3-20)
    return val

ans = change(lst)
for elem in ans:
    print(elem,end=' ')