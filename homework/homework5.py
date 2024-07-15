'''2. Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.'''

immutable_var = 1, 2, 3, [1, 5], True
print(immutable_var)
#immutable_var[1] = 7
#print(immutable_var)   # Кортеж не поддерживает назначение элементов, кортежи не изменяется, можно заменить элементы списка(list), только поменять

mutable_list = [1, 4, 5, 1, 2, 3]
mutable_list[1] = 2
mutable_list[3] = 4
mutable_list.sort()
print(mutable_list)

