n = int(input())

def string(n):
    sen = 'Coding is my favorite hobby!'
    if n>0:
        print(sen)
        string(n-1)

string(n)