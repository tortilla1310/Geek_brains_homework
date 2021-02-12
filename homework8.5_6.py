class OfficeWarehouse:
    def __init__(self, name, price, color, *args):
        self.name = name
        self.price = price
        self.color = color
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Наименование': self.name, 'цена ': self.price, 'цвет': self.color}

    def __str__(self):
        return f'{self.name} цена {self.price} цвет {self.color}'

    def reception(self):
        try:
            unit = input(f'Введите наименование оргтехники ')
            unit_price = int(input(f'Введите цену '))
            unit_color = input(f'Введите цвет ')
            unique = {'Наименование': self.name, 'цена ': self.price, 'цвет': self.color}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Список оргтехники {self.my_store}')
        except:
            return f'Ошибка'

        print(f' Чтобы выйти - q')
        q = input(f' ---> ')
        if q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'  Склад {self.my_store_full}')
            return f'Выход'
        else:
            return OfficeWarehouse.reception(self)

class OfficeEquipment:
    def __init__(self, name, price, color, *args):
        self.name = name
        self.price = price
        self.color = color
        self.amount = []


class Printer(OfficeWarehouse):
    def to_print(self):
        return f'Напечатать что-нибудь'


class Scanner(OfficeWarehouse):
    def __init__(self, name, price, color, amount):
        super().__init__(name, price, color, amount)


class Xerox(OfficeWarehouse):
    def __init__(self, name, price, color, amount):
        super().__init__(name, price, color, amount)


unit_1 = Printer('hp', 2000, 'red', 3)
unit_2 = Scanner('Epson', 5000, 'white', 8)
unit_3 = Xerox('Xerox', 9800, 'silver', 5)
print(unit_1)
print(unit_2)