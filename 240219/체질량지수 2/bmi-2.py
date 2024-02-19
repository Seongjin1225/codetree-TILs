# bmi 공식 => weight/height*height
height, weight = tuple(map(int,input().split()))

bmi = weight*(100**2)/height**2
floor_bmi = int(bmi)
fin_bmi_floor = f'{floor_bmi:.0f}'
# print(fin_bmi_floor)

if int(fin_bmi_floor) >= 25:
    print(fin_bmi_floor)
    print('Obesity')
else:
    print(fin_bmi_floor)