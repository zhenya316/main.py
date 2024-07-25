# def, функция шаблон кода для упрашения работы. Лучше называть их понятными названиями, дающее как можно больше понимания её функуонала
# Функция эта обьект, на вход принимает переменные. Есть принимающие, возвращающие, обычные, анонимные
# Функция важный элемент программирования, фундаметальный! нужно уметь их писать, потренироваться при выполнение заданий
# Ещё есть классы - @, что то похожее на функции
def say_hello(name):        # принимающая функция
    print('Hello', name)

say_hello('Zhenya')         # вызов функции, много раз можно вызвать

import random
def lottery(*args, **kwargs):                          # возвращающая функция
    tickets = [1, 2, 3, 4, 5, 6, 7]                    # *args - если не знаем сколько будет обычных параметров
    win = random.choice(tickets)                       # можно передать много параметров
    tickets.remove(win)                                # **kwargs - для именнованных параметров
    win1 = random.choice(tickets)
    print(*args)
    return win, win1                          # return - прекращает функцию и возвращает результат


a, b = lottery([1,2],1, 3)
print(a, b)

def test(a=2, b=True):          # Принимающая функция, можно написать переменные по умолчанию, их можно переназначить
    print(a, b)

test(3, False)

test(*[1, 2])                   # * - Символ распаковки. ** - распаковка словаря