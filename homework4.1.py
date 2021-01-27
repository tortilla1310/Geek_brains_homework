from sys import argv

script_name, work_in_hours, rate_in_hours, bonus = argv

print(f'Имя скрипат: {script_name}, выработка в часах: {work_in_hours}, ставка в час: {rate_in_hours}, премия: {bonus}')


#Функцию для удобства разместила в одном документе с импортированным модулем.
#Когда выполняла задания, функция была в соседнем файла, т.к. совместно с модулем она не идет
def my_func():
    work_in_hours = int(input('введите выработку в часах '))
    rate_in_hours = int(input('введите ставку в час '))
    bonus = int(input('введите премию '))
    result = work_in_hours * rate_in_hours + bonus
    return result


print(my_func())

