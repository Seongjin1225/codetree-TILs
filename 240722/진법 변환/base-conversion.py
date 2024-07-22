n,m = tuple(input().split())
ans = 0

if int(m) < 10:
    for i in range(len(str(n))-1,-1,-1):
        ans += (int(m)**(len(n)-i-1))*int(str(n)[i])
    print(ans)
else:
    for i in range(len(str(n))-1,-1,-1):
        if n[i].isdigit():
            ans += (int(m)**(len(n)-i-1))*int(str(n)[i])
        else:
             ans += (int(m)**(len(n)-i-1))*(ord(n[i])-55)
    print(ans)