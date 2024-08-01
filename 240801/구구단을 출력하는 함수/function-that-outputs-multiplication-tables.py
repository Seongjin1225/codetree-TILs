num = list(map(int,input().split()))
num = sorted(num)

def nine(num):
    for i in range(min(num),max(num)+1):
        if i == num[1]:
            continue
        for j in range(1,10):
            print(f'{i} * {j} = {i*j}')
nine(num)