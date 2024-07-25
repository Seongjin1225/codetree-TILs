# num = int(input())
# num = list(str(num))
# lst_num = list(map(int,num))
# n = len(lst_num)
# ans = []

# for i in range(n):
#     temp = []
#     while lst_num[i] > 0:
#         temp.append(lst_num[i] % 2)
#         lst_num[i] //= 2
#     if not temp: 
#         temp.append(0)
#     ans.extend(temp) 
# print(ans)

# 8진수 입력 받기
octal_num = input()

# 8진수 각 자릿수를 2진수로 변환
binary_str = ''
for digit in octal_num:
    binary_str += format(int(digit), '03b')

# 0인 경우를 제외하고 1로 시작하는 2진수 출력
binary_str = binary_str.lstrip('0')
if binary_str == '':
    binary_str = '0'

print(binary_str)