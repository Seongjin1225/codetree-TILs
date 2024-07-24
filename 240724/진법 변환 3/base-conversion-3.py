n = int(input())
num = list(str(n))
ans = []

for digit in num:
    decimal_value = int(digit) 
    binary_digits = []
    
    while decimal_value > 0:
        binary_digits.append(decimal_value % 2)
        decimal_value //= 2
    
    while len(binary_digits) < 3:
        binary_digits.append(0)
    
    binary_digits.reverse()  
    ans.extend(binary_digits)


result = ''.join(map(str, ans)).lstrip('0')
print(result)