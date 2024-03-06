a,b = input().split()
val, val_2 = '', ''

for i in a:
    if i.isdigit():
        val += i

for j in b:
    if j.isdigit():
        val_2 += j

print(int(val)+int(val_2))