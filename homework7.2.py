class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_result_a(self):
        return self.size / 6 + 0.5

    def get_result_b(self):
        return self.height * 2 + 0.3
    @property
    def get_result_full(self):
        return str(f'Общая площадь ткани '
                   f'{round(self.size / 6 + 0.5) + round(self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.result_a = round(self.size /6 + 0.5 )

    def __str__(self):
        return f'Площадь ткани на пальто {self.result_a}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.result_b = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.result_b}'

coat = Coat (7, 8)
suit = Suit(3, 9)

print(coat)
print(suit)
print(coat.get_result_a())
print(suit.get_result_b())
print(coat.get_result_full)
print(suit.get_result_full)