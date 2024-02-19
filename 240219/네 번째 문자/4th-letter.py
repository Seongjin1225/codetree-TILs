n,word = tuple(input().split())
n = int(n)

words = []
for i in range(n):
    words.append(input())

ans = []
for elem in words:
    if elem[3] == word:
        ans.append(elem)

print(len(ans))
for word in ans:
    print(word)