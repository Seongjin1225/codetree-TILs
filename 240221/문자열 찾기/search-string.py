sentence = input()
cnt,cnt_2 = 0,0

for i in range(len(sentence)-2):
    if sentence[i:i+3] == 'KOI':
        cnt += 1
    if sentence[i:i+3] == 'IOI':
        cnt_2 +=1

print(cnt, cnt_2)