height, weight = tuple(map(int,input().split()))

bmi = (weight/(height**2))*10000
if bmi >= 25:
    print(f'{bmi:.0f}')
    print('Obesity')
else:
    print(f'{bmi:.0f}')