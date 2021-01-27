def fact(n: int):
    a = 1
    for i in range(1, n+ 1):
        a *= i
        yield a


n = int(input("факториал какого числа высчитать?\n"))


for el in fact(n):
    print(el)
