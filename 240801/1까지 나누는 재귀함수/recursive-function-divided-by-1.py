n = int(input())
ans = [n]

def divide(num):
    if num > 1:
        if num%2 == 0:
            num //= 2
            ans.append(num)
            divide(num)
        else:
            num //= 3
            ans.append(num)
            divide(num)
    return ans

val = divide(n)
for elem in val:
    print(elem,end=' ')