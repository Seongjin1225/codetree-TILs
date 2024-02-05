height, weight = tuple(map(int,input().split()))
height = height/100
bmi = weight/(height**2)
if bmi >= 25:
    print(f'{bmi:.0f}')
    print('Obesity')
else:
    print(f'{bmi:.0f}')