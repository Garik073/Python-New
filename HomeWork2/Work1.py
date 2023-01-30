import os
os.system('cls')
coin = int(input('Введите количество монет: '))
print("Введите значения от 0 до 1. Где 0 это гербом вниз а 1 это решкой вверх  ")
i = 1
emblem = 0
for _ in range(coin):
    print( i, "-вое значение: ")
    i +=1
    count = int(input())
    if count == 0:
        emblem +=1
print("Количество монет которые нужно перевернуть",emblem)             

