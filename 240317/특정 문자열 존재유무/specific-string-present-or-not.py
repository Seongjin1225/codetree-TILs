n, word = input().split()

for _ in range(int(n)):
    sen = input()
    if word in sen:
        print(sen)