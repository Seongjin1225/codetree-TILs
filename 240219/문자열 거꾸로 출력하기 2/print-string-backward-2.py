n = int(input())
words = []  # 입력 단어 저장할 빈 리스트

for i in range(n):
    words.append(input())

for elem in words:
    elem = elem[::-1]
    print(elem)