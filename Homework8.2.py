class DivisionZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return f'Делить на ноль нельзя'

divide = DivisionZero(20,40)
userdata = int(input('ВВедите первое число '))
userdata2 = int(input('ВВедите второе число '))
print(DivisionZero.divide_null(userdata, userdata2))
print('%.2f' % DivisionZero.divide_null(userdata, userdata2))
print(divide.divide_null(userdata, userdata2))
print('%.2f' % divide.divide_null(userdata, userdata2))