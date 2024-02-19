n = int(input())

words = []
for i in range(n):
    words.append(input())
a = input()

ans = []
cnt = 0
for word in words:
    if word.endswith(a):
        ans.append(word)
        cnt += 1

print(cnt)
for elem in ans:
    print(elem)