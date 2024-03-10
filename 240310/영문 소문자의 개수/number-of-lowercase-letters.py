n = int(input())
sen = input().split()

frequency = {}

for elem in sen:
    if elem.isupper():
        idx = sen.index(elem)
        sen_2 = sen[:idx]
        for elem in sen_2:
            if elem in frequency:
                frequency[elem] += 1
            else:
                frequency[elem] = 1

for key, value in sorted(frequency.items()):
    print(f"{key} : {value}")