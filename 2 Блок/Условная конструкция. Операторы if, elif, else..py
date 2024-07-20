# Условная конструкция. Операторы if, elif, else. начало условий всегда начинаеться с if(если).
# При решение задач в начале пишем самое маловероятное событие. and - выполняеться 2 условия это и это,  or - выполняеться одно из условий или то или то
number = int(input('Введите число: '))          # Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число не подходит')