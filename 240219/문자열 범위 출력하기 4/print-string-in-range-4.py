n = int(input())
word = input()

if n > len(word):
    print(word)
else:
    print(word[:n])