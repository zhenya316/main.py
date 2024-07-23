'''Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки
(True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []     # Простые числа
Not_primes = [] # составные
numbers.remove(1)
for i in range(len(numbers)):
    is_prime = True                     # Flag - булевая переменная меняющая своё значение в процессе проверки, на С часто используют
    a = 0
    for j in range(1, numbers[i] + 1):
        if numbers[i] % j == 0:
            a += 1
    if a >= 3:
        is_prime = False
    if is_prime:
        Primes.append(numbers[i])
    else:
        Not_primes.append(numbers[i])
print('Primes:', Primes)
print('Not_primes:', Not_primes)


