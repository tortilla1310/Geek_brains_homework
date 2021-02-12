class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        new_cell_number = self.number + other.number
        new_cell = Cell(new_cell_number)
        return new_cell

    def __sub__(self, other):
        if self.number > other.number:

            new_cell_number = self.number - other.number
            new_cell = Cell(new_cell_number)
            return new_cell
        else:
            raise Exception("Ошибка")

    def __mul__(self, other):
        new_cell_number = self.number * other.number
        new_cell = Cell(new_cell_number)
        return new_cell

    def __truediv__(self, other):
        new_cell_number = self.number // other.number
        new_cell = Cell(new_cell_number)
        return new_cell

    def make_order(self, number_per_row):
        full_rows_amount = self.number // number_per_row
        residual_amount = self.number % number_per_row

        full_row_string = "*"*number_per_row + "\n"
        full_row_final_string = full_row_string * full_rows_amount

        final_string = full_row_final_string + "*"*residual_amount
        return final_string


a = Cell(1700)
b = Cell(12)
print((a+b).number)
print((a-b).number)
print((a*b).number)
print((a/b).number)

print(a.make_order(500))