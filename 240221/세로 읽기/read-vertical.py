# 다섯 개의 단어를 입력 받음
words = [input() for _ in range(5)]

# 가장 긴 단어의 길이를 구함
max_length = max(len(word) for word in words)

# 단어를 세로로 출력 형식에 맞게 변환하여 저장
vertical_words = [''.join(word.ljust(max_length)) for word in words]

# 변환된 문자열을 세로로 출력
for i in range(max_length):
    for word in vertical_words:
        print(word[i], end='')