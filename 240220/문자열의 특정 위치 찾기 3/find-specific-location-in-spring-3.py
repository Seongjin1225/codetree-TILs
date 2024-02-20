sentence = input()
word = input()

for i, w in enumerate(sentence):
    if w == word:
        print(i+1)
        break
    if word not in sentence:
        print('Not Found')