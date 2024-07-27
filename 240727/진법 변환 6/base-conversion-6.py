# a,n,b = input().split()
# tmp = 0
# leng = len(n)
# ans = []

# # n을 10진수로 변환
# if n.isalpha():
#     num = ord(n)-87
#     for i in range(leng-1,-1,-1):
#         tmp += int(num[i])*(2**(leng-i-1))
# else:
#     for i in range(leng-z1,-1,-1):
#         tmp += int(n[i])*(2**(leng-i-1))

# # 10진수를 b진수로 변환
# while True:
#     if tmp < int(b):
#         ans.append(tmp)
#         break
#     val = tmp%int(b) 
#     if val < 10:
#         ans.append(tmp%int(b))
#     else:
#         ans.append(chr(val+87))
#     tmp //=int(b)

# ans.reverse()
# for elem in ans:
#     print(elem,end='')

def convert_to_decimal(n, base):
    decimal_value = 0
    length = len(n)
    for i in range(length):
        digit = n[length - 1 - i]
        if '0' <= digit <= '9':
            decimal_value += (ord(digit) - ord('0')) * (base ** i)
        else:
            decimal_value += (ord(digit) - ord('a') + 10) * (base ** i)
    return decimal_value

def convert_from_decimal(decimal, base):
    if decimal == 0:
        return "0"
    
    result = []
    while decimal > 0:
        remainder = decimal % base
        if remainder < 10:
            result.append(chr(remainder + ord('0')))
        else:
            result.append(chr(remainder - 10 + ord('a')))
        decimal //= base
    
    return ''.join(result[::-1])

# 입력 받기
a, n, b = input().split()
a = int(a)
b = int(b)

# n을 10진수로 변환
decimal_value = convert_to_decimal(n, a)

# 10진수를 b진수로 변환
result = convert_from_decimal(decimal_value, b)

# 결과 출력
print(result)