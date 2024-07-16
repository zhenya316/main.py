phone_book = {'Denis': 89001122333, 'Masha': 89003332211}   # key:value - кллюч и значение, ключ не может быть изменяемым типом данных, а значени может
print(phone_book)                                           # Словарь не упорядочный, всегда разная последовательность элементов
phone_book['Denis'] = 12345678999                           #словарь - {} dict, изменяемый
print(phone_book['Denis'])
print(type(phone_book))
phone_book['Anton'] = 854112645241      # если нет в словаре, добавляет новый ключ
print(phone_book)
del phone_book['Masha']     # удалил элемент по ключу
print(phone_book)

phone_book.update({'Max': 798987444444, 'Alex': 8744551226})    #метод update множественное изменения
print(phone_book)
print(phone_book.get('Kamila', 'такого ключа нет'))     # Метод get, если значения есть возвращает Noon, можно задать значение Noon
print(phone_book)
a = phone_book.pop('Anton')     # удаляет значение и его можно записать, для списков так же работает только через индекс,
print(phone_book)
print(a)
list = [1, 5, 5, 7]
a = list.pop(0)
print(a)
print(list)
print(phone_book.keys())        # метод  keys - выводит все ключи словаря
print(phone_book.values())      # метод  values - выводит все значения словаря
print(phone_book.items())   # метод items - выводит словарь со значениями
phone_book['Denis'] = [12132142154, 12412125467547]
print(phone_book)                      # В Вэбе часто используют словари
set_ = {1, 2, 3, 6, 7, 1, 2, 3, True}       # множества или кортеж, хранит только уникальные значения
print(set_)
list = [1, 2, 3, 1, 2, 3, 5]
list = set(list)
print(list)                # перевёл список в множество
#print(list[0])             # нельзя обратиться к конкретному элементу по индексу, перебор с помощью циклов
list.discard(1)             # удаление по элементу
print(list)
list.remove(2)              # удаление элемента, но выдаст ошибку если элемента нет. Можно использовать pop()
print(list)
list.add(1)             # добавление
print(list)