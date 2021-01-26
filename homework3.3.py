def my_func(number1, number2, number3):
    return number1+number2+number3 - min


number1 = int(input('введите первое число '))
number2 = int(input('введите второе число '))
number3 = int(input('введите третье число '))
if number1 < number2: min = number1
else:
    min = number2
if number3 < min: min = number3


print(my_func(number1, number2, number3))







