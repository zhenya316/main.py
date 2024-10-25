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
