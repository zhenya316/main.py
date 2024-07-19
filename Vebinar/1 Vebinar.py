a = 20
b = 12
c = 1
v= a * b - c
print(a+c)

#списки
a = [1,5, 3, 7,]
print(max(a))       # max - максимальное значение списка
print(min(a))       # min - минимальное значение списка
print(len(a))       # len - длина списка
print(sorted(a))    # Sorted - вывести сортированный список, он не изменился

print(a)
a.sort()            # .sort - отсортировать список, он изменился
print(a)
a.reverse()         # .reverse - перевернуть список задом на перёд
print(a)
# Словари

d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}        #{key:value} - словарь
keys = list(d.keys())           # .keys - вывести все ключи словаря
value = list(d.values())        # .values - вывести все значения словаря
print(keys)
print(value)

n = dict(zip(keys, value))      #zip - соеденяет два списка в словарь по символу
m = list(zip(keys, value))      #zip - соеденяет два списка в кортежи
print(n)
print(m)
print(type(m))

print(round(42.13 - 42, 2 ))         #round - округляет до определённых чисел после запятой, второй число определяет количество