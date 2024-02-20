n = int(input())
num = list(map(int,input().split()))
k = int(input())

yak = []
bae = []

for elem in num:
    if k%elem == 0:
        yak.append(elem)
    if elem % k == 0:
        bae.append(elem)
print(sum(yak))
print(sum(bae))