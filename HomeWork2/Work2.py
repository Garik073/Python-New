import os
os.system('cls')
s = int (input("Введите число S: "))
p = int (input("Введите число P: "))
x = (s-int((s**2-4*p)**0.5))//2
y = (s+int((s**2-4*p)**0.5))//2
if x + y ==s and x * y == p:  
     print(x, y)