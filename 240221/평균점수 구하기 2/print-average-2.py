n = int(input())
scores = tuple(map(float,input().split()))

print(f'{sum(scores)/len(scores):.1f}')