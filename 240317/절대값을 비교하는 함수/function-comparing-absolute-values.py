n = int(input())
arr = []

for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))


def perfect(lst):
    for elem in lst:
        print(max(abs(elem[0]), abs(elem[1])))

perfect(arr)