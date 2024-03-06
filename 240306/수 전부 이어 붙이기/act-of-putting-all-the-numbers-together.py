n = int(input())
arr = list(map(int,input().split()))

val = ''
for elem in arr:
    val += str(elem)
 
i = 0
while i < len(val):
    print(val[i:i+5])
    i+=5