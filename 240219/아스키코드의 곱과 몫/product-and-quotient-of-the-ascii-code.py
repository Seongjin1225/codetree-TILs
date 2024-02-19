a,b = tuple(input().split())

ascii_a = ord(a)
ascii_b = ord(b)

multi = ascii_a * ascii_b

if ascii_a > ascii_b:
    divid = ascii_a%ascii_b
else:
    divid = ascii_b%ascii_a

print(multi, divid)