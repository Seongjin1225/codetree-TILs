sentence = input()

sen = sentence.split(' ')

for i in range(len(sen)):
    if i%2 !=0:
        print(sen[i])