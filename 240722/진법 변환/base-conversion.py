n,m = tuple(input().split())
ans = 0

if int(m) < 10:
    for i in range(len(str(n))):
        ans += (int(m)**i)*int(str(n)[i])
    print(ans)
else:
    for i in range(len(str(n))):
        ans += (int(m)**i)*(ord(n[i])-55)
    print(ans)