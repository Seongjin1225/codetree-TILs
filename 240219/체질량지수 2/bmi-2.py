# bmi 공식 => weight/height*height
height, weight = tuple(map(int,input().split()))

bmi = weight*(100**2)/height**2
fin_bmi = f'{bmi:.0f}'

if int(fin_bmi) >= 25:
    print(fin_bmi)
    print('Obesity')
else:
    print(fin_bmi)