n = int(input())

words = []

for i in range(n):
    words.append(input())

words.sort()
print(words[0])