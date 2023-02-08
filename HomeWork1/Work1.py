chislo = int(input("Введите число: "))
sum = 0
while (chislo != 0):
    sum = sum + chislo % 10
    chislo = chislo // 10
print("Сумма цифр числа равна: ", sum)