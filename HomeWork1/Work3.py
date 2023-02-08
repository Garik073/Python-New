a = [int (i) for i in input("Введите 6 -ое число ")]
if sum(a[:3]) == sum(a[3:]):
    print('lucky')
else:
    print('unlucky')