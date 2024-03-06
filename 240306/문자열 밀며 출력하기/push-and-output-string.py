word = input()

i = 0
while True:
    if i == 0:
        print(word)
    else:
        wor = word[1:] + word[0]
        print(wor)
        word = wor
    i+=1
    if i == len(word)+1:
        break