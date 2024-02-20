n = int(input())
word = tuple(input().split())
# 3,5,8 -> index 2,4,7

for i in range(len(word)):
    if i + 1 == 3:
        print(word[i],end=' ')
    if i+ 1 == 5:
        print(word[i], end=' ')
    if i + 1 == 8:
        print(word[i])