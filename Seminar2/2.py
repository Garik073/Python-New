num = int(input())
f_1 = 0
f_2 = 1
i = 2
while  f_2 <= num:
    if num == f_2:
        print(i)
        break
    f_1, f_2 = f_2, f_1 + f_2
    i += 1
else:
    print(-1) 