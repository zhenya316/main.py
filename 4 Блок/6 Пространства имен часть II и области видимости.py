import math

a = 5           # глобальное пространство имён
c = 1
def square(x):
    global a
    d = 1
    a = x ** 2
    print(locals())
    return a

b = square(2)
print(a)
print(b)
#print(d)        # пространство имён работает изнутри наружу, в локальное пространство можно взять что то из глобального наоборот нельзя
print(globals())

print(math.sqrt(a))
#Область видимости-это, по сути, та часть кода, где у нас переменная доступна, и мы можем её использовать.
# Существует всего 4 области видимости: Встроенная, Глобальная, Объемлющая, локальная. С глобальной мы с вами уже знакомы. То есть вот наша переменная «а»,
# она находится в глобальной области видимости

'''
Поиск переменных или функций происходит изнутри наружу, наоборот не может быть, в глобальном пространстве нельзя использовать переменные из локальной, а наоборот можно
с помощью команды global, в локальном пространстве можно использовать из Объемлющей с помощью команды - nonlocal
Встроенное
    Глобальное
        Объемлющее
            Локальное
'''

