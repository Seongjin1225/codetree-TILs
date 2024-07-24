num, way = list(map(int, input().split()))
ans = []
two = [2, 8]

map_num = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

if way in two:
    while num > 0:
        ans.append(num % way)
        num //= way
else:
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            ans.append(str(remainder))
        else:
            ans.append(map_num[remainder])
        num //= 16

ans.reverse()
print(''.join(map(str, ans)))