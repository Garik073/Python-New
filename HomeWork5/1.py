#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('cls')

def rekursia(A, degree):
    if (degree == 1):
        return (A)
    if (degree != 1):
        return (A ** degree)
A = int(input("Введите число: "))
degree = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", rekursia(A, degree))