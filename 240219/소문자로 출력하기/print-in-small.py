import re
sentence = input()

ans = ''.join(re.findall('[a-zA-Z]', sentence)).lower()

print(ans)