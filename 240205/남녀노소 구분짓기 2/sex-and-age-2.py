gender = int(input())
age = int(input())

if gender == 0:
    if age >= 19:
        print('M')
    else:
        print('B')
else:
    if age >= 19:
        print('W')
    else:
        print('G')