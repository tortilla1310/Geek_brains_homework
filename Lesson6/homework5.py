class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка объекта {self.title}'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка объекта {self.title}'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка объекта {self.title}'


pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Handle('маркером')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
