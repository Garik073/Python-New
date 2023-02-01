print('Введите размер шоколадки m x n и количество долек k')
n=int(input('Введите n '))
m=int(input('Введите m '))
k=int(input('Введите k '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')