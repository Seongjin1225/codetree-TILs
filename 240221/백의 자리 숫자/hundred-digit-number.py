n = int(input())
arr = tuple(map(int,input().split()))

dic = {
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
}

for elem in arr:
    if elem <= 99:
        dic['0']+=1
    else:
        ans = str(elem)[0]
        dic[ans]+=1

for key, value in dic.items():
    if value != 0:
        print(key, '-', value)