n = int(input())

sen = ''
for i in range(n):
    word = input()
    sen += word

cnt = len(sen)//2
print(sen[:cnt])
print(sen[cnt:])