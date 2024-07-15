a = 20
b = 12
c = 1
v= a*b - c
print(a+c)

#списки
a = [1,5, 3, 7,]
print(max(a))
print(min(a))
print(len(a))
print(sorted(a))

print(a)
a.sort()
print(a)
a.reverse()
print()
# Словари

d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
keys = list(d.keys())
value = list(d.values())
print(keys)
print(value)

n = dict(zip(keys, value))
m = list(zip(keys, value))
print(n)
print(m)

print(round(42.13 - 42, 2 ))         #round - округляет до определённых чисел после запятой