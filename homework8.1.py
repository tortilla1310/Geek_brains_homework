class Data:

    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'Все хорошо'
                else:
                    return f'неправильный год'
            else:
                return f'Неправльный месяц'
        else:
            return f'Неправльный день'
    def __str__(self):
        return f'Текущая дата: {Data.extract(self.day_month_year)}'

today = Data('15 - 02 - 2000')
print(today)
print(today.valid(32, 1, 2020))
print(Data.valid(1, 2, 2030))
print(Data.extract('1 - 15 - 2020'))