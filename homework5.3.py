my_list = {'Иванов': 25000, 'Дятлов': 17300, 'Петров': 2750, 'Сидоров': 19870}
try:
    my_file = open('test-2.txt', 'a')
    for surname, salary in my_list.items():
        my_file.write(surname + ':' + str(salary) + '\n')
except IOError:
    print('Ошибка')
finally:
    my_file.close()

sum = 0
count = 0
people = []
with open('test-2.txt', 'r') as my_file:
    for line in my_file:
        print(line, end = '')
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            people.append(tokens[0])
        sum += int(tokens[1])
        count += 1
result = sum / count
print(f'people: {people}')
print(f'среднее: {result}')

