sci, soci = tuple(map(int,input().split()))
b_sci, b_soci = tuple(map(int,input().split()))

if sci > b_sci and soci > b_soci:
    print(1)
else:
    print(0)