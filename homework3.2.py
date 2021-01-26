def userData(**datas):
    print(datas)


userData(name=input('введите имя '),  surname=input('введите фамилию '), year=int(input('введите год рождения ')), city=input('введите город проживания '), email=input('введите электронный адрес '), phone=int(input('введите номер телефона')))