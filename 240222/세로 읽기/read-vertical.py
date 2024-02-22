n = 5
max_len = 0
words = []

# 단어를 입력받고 최대 길이를 찾음
for i in range(n):
    word = input()
    words.append(word)
    max_len = max(max_len, len(word))

# 각 단어를 최대 길이에 맞게 오른쪽 정렬하여 출력
for i in range(max_len):
    for word in words:
        if i < len(word):
            print(''.join(word[i]),end='')