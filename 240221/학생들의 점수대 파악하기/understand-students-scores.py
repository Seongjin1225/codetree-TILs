n = int(input())
arr = tuple(map(int,input().split()))

scores = {
    '100':0,
    '90':0,
    '80':0,
    '70':0,
    '60':0,
    '50':0,
    '40':0,
    '30':0,
    '20':0,
    '10':0,
}

for score in arr:
    if score < 10:
        continue
    elif score == 100:
        scores[str(score)] += 1
    else:
        val = str(score)[0]
        scores[str(int(val)*10)] += 1

for key, value in scores.items():
    if value != 0:
        print(key, '-', value)