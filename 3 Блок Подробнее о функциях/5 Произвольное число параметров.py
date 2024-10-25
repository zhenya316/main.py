# def test_func(*params):
#     print("Тип:", type(params))               # * - если нужно множественное получение позиционных параметров
#     print("Аргумент:", params)
#
# #
# # test_func(1, 2, 3, 4)
#
# def summator(txt, *values, type="sum"):       # (позиционный параметр, множество позиционных параметров, именной параметр), именной параметр не ставиться перед позиционным или перед *
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
#
#
# print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))        # подсчёт суммы чисел


# def info(value, *types, names_author="Den", **values):    # принимает (позиционный параметр, множество позиционных параметров, именной параметр, множество именнованный параметров)
#     print("Тип:", type(values))
#     print("Аргумент:", values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
#
# info("Пример использования параметров всех типов", 2, 3, 4, names_author="Denis", name="Den", course="Python")


def my_sum(n, *args, txt="Сумма чисел"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)


my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")