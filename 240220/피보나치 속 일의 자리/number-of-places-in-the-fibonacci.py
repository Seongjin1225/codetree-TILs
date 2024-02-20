def generate_sequence(n, first, second):
    sequence = [first, second]  
    for _ in range(2, n):  # 세 번째 항부터 n번째 항까지 반
        next_term = (sequence[-2] + sequence[-1]) % 10   
        sequence.append(next_term)  
    return sequence

# 사용자로부터 n과 첫 번째, 두 번째 항을 입력 받음
n = int(input())
first,second = tuple(map(int,input().split()))

# 수열을 생성하고 출력
sequence = generate_sequence(n, first, second)
for elem in sequence:
    print(elem,end=' ')