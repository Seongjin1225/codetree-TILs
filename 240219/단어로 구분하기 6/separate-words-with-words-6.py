sentence = input()

sen = sentence.split(' ')

for i in range(len(sen)):
    if (i+1)%3 == 0:
        print(sen[i])