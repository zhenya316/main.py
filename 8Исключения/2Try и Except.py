# try:
#     # пишем код с возможной ошибкой
# except:
#     # выполняется если произошла ошибка
# Перехватываем ошибку
try:
    a = c+b
    i = 0
    print(10/i)     # на этой строке когда произошла ошибка, перешёл на блок except:, не выполняя ошибочный код
    print('готово')
except (ZeroDivisionError, NameError):      # Указали какая именно будет ошибка, указав её класс, другой класс ошибок не видит
    print('что то пошло не так')
except:
    print('какая то ошибка')            # Можно указать несколько или написать второй блок except, их можно писать несколько

try:
    m = 5/0
except ZeroDivisionError as qwe:
    print(f'ошибка - {qwe}')            # Выводиться описание класса, почему ошибка

try:
    file = open('qweqwrq.txt')
except OSError as qwer:
    print(f'ошибка - {qwer}, параметры {qwer.args}')
else:       # Если ошибки не возникло, не обязательно
    print('всё гуд, ошибки такой то нет')
finally:    # выполняется всегда в конце, не обязательно
    print('ошибка в другом месте')
