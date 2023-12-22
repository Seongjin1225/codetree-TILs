n = int(input())
arr = list(map(int,input().split()))
new_arr = []
for elem in arr:
    if elem%5!=0 and elem%7!=0:
        new_arr.append(elem)
sum_val = sum(new_arr)
avg = sum_val/len(new_arr)

print(sum_val)
print(f'{avg:.1f}')