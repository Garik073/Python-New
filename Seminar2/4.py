import os
os.system('cls')

total = int(input())
max = min = int(input("Ves: "))

for _ in range(total - 1):
    count = int(input())
    if count > max:
        max =count
    if count < max:
        min = count
print(min, max)            