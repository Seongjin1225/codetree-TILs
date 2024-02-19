words = []
cnt = 0

while True:
    word = input()
    if word == '0':
        break
    cnt += 1
    if cnt % 2 == 0:
        words.append(word)

print(cnt)
for word in words:
    print(word)