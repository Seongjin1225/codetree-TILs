arr = list(map(float,input().split()))

def calc(lst):
    print(f'{sum(lst):.0f}')
    print(f'{sum(lst)//3:.0f}')

calc(arr)