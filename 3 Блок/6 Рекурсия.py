# рекурсия, функция вызывающая сама себя, можно решить задачу без применения рекурсии, обычным циклом
# Посмотреть наглядно в каком порядке выполняется рекурсия можно здесь - https://pythontutor.ru/lessons/inout_and_arithmetic_operations/
# def summa(n):         # рекурсия
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
#
# print(summa(5))
def recursion():
    recursion()

recursion()
# stack = []
# stack.append(1)
# print('Добавили элемент' , stack)
# stack.append(2)
# print('Добавили элемент' , stack)
# stack.append(3)
# print('Добавили элемент' , stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)