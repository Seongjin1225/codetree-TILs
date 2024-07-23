word1 = input()
word2 = input()
n = len(word2)

for i in range(len(word1)-1):
    if word1[i:i+n] == word2:
        word1 = word1.replace(word2,'')
print(word1)