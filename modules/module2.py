from dis import dis     # чтобы показать байт код в терминале


def say_hi():
    print('Привет я из функции во втором модуле')


def main():
    a = 5
    b = 10
    print('Привет')


if __name__ == '__main__':      # условия для запуска определённой части кода
    main()


dis(say_hi)