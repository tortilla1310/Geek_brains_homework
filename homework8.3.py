class CheckNumbers:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                value = int(input('Введите число или текст. Если захотите выйти, напишите текст, затем слово stop'))
                self.my_list.append(value)
                print(f' Содержание списка - {self.my_list}')
            except:
                print(' Вы ввели текст, а нужно число, попробуйте еще раз ')

                userdata = input('Введите число или пропишите stop для выхода ')
                if userdata == 'stop':
                    print('Вы вышли')
                    break


try_except = CheckNumbers(1)
print(try_except.my_input())