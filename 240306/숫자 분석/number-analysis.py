num = int(input())

val = str(num)[::-1]

val_2 = 0
for elem in str(num):
    val_2 += int(elem)

print(val, val_2)