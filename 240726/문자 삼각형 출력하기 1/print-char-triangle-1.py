n = int(input())
num = 65
step = n-1
arr = [['' for _ in range(n)]for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            if  j < n-i-1:
                arr[i][j] = " "
            else:
                arr[i][j] = chr(num)
                num+=1
        elif i !=0:
            if j < n-i-1:
                arr[i][j] += " "
            else:
                start_num = num 
                if j == 1:
                    arr[i][j] = chr(num)
                    num += step
                else:
                    arr[i][j] = chr(num)
                    step -= 1
                    num += step
                    if num > 90:
                        num = (num - 90) + 64
                num = start_num + 1 
                step = n- 1 

# for elem in arr:
#     print(''.join(elem))  

# for i in range(n):
#     print(" " * (2*(n-(i+1))), end=" ")
#     if i == 0:
#         print(chr(num))
#         num += 1
#     else:
#         start_num = num  
#         for j in range(i + 1):
#             if j == 0:
#                 print(chr(num), end=" ")
#                 num += step
#             else:
#                 print(chr(num), end=" ")
#                 step -= 1
#                 num += step
#                 if num > 90:
#                     num = (num - 90) + 64

#         num = start_num + 1 
#         step = n- 1 
#         print()