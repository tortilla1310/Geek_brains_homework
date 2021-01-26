def my_func(x, y):
   if y < 0:
       print(x**y)
   else:
       print(input('вы ввели не отрицательное число'))

x = int(input('введите положительное число '))
y = int(input('Введите отрицательное число '))
my_func(x, y)


def my_func(x, y):
    if x == 0:
        return 0
    if y < 0:
        x = 1.0 / x
        y = -y
    res = 1
    while y > 0:
        res= res * x
        y = y - 1
    return res


x = int(input('введите положительное число '))
y = int(input('Введите отрицательное число '))
print('%.2f' % my_func(x, y))