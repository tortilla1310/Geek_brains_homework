from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


list = [el for el in range(99, 1001) if el % 2 == 0]
new_list = reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])

print(f'список элементов: {list}')
print(f'результат умножения: {new_list}')


