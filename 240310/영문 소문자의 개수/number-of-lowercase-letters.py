n = int(input())
sen = input().split()

frequency = {}

for elem in sen:
    if elem.isupper() or elem.isdigit():
        idx = sen.index(elem)
        sen = sen[:idx]
        break

for el in sen:
    if el in frequency:
        frequency[el] += 1
    else:
        frequency[el] = 1

for key, value in sorted(frequency.items()):
    print(f"{key} : {value}")