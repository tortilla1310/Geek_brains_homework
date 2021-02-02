user_input = input('Введите числа через пробел ')
numbers = [int(i) for i in user_input.split() if i.isdigit()]

with open('test-3.txt', 'r+') as file_obj:
    print(sum(numbers))
    file_obj.write(str(numbers))