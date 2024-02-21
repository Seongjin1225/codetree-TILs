n = int(input())

results = tuple(map(int,input().split()))

dice = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0
}

for num in results:
    dice[str(num)] += 1

for key,value in dice.items():
    print(key, '-', value)