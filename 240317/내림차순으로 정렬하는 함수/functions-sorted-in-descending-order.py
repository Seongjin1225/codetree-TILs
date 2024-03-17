n = int(input())
lst = list(map(int,input().split()))

def sorting(arr):
    arr.sort(reverse=True)
    for elem in arr:
        print(elem,end=' ')

sorting(lst)