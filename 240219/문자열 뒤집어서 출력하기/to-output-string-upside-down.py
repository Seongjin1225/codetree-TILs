words = []

for i in range(4):
    words.append(input())

for i in range(len(words)-1,-1,-1):
    print(words[i][::-1])