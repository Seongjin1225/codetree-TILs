n = int(input())

for _ in range(n):
    word = input()
    if word.isalpha():
        print(word)
    else:
        print(ord(word))