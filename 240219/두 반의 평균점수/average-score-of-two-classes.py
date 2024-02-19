n = int(input())
scores = list(map(int,input().split()))
a, b= tuple(map(int,input().split()))

avg = (scores[a-1] + scores[b-1])/2

print(f'{avg:.1f}')