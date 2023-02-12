import os
os.system('cls')

num = int(input())
max_row, current_row = 0
for i in range(num):
    temp = int(input())
    if temp > 0:
        current_row += 1
    else:
        if current_row > max_row:
         max_row, current_row = current_row , 0
         current_row  = 0
print(max_row)

