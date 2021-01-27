from itertools import count
from itertools import cycle

for el in count(int(input('введите число '))):
    if el > 20:
        break
    print(el)

count = 0
list = ['ABCD, 1, 2, none']
for el in cycle(list):
    count += 1
    if count > 30:
        break
    print(list)

