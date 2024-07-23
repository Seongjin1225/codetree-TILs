word1 = input()
word2 = input()
n = len(word2)

while word2 in word1:
    word1 = word1.replace(word2, '')

print(word1)