def my_func():
    try:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))
        return number1 / number2 
    except ZeroDivisionError:
        return 'на ноль делить нельзя'


print(my_func())
