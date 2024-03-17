n = int(input())
arr = list(map(int,input().split()))

def perfect(lst):
    val = 0
    for elem in lst:
        val += abs(elem)
    return val

print(perfect(arr))