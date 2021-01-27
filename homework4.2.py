numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_numbers = [el for num, el in enumerate(numbers) if numbers[num - 1] < numbers[num]]
print('Исходный список', numbers)
print('Новый список', new_numbers)
