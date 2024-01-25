arr = []
for _ in range(5):
    arr.append(float(input()))

for elem in arr:
    r_elem = round(elem,3)
    print(f'{r_elem:.3f}')