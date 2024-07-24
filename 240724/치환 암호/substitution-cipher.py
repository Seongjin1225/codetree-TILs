sen = input()
code = input()
arr, result = [], []
num = 97
for i in range(len(code)):
    arr.append([chr(num),code[i]])
    num+=1

for i in range(len(sen)):
    if sen[i] != ' ':
        for j in range(len(arr)):
            if sen[i] == arr[j][1]:
                result.append(arr[j][0])
    else:
        result.append(' ')

ans = ''.join(result)
print(ans)