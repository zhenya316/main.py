'''food = ['apple', 'coconut', 'banana']   # списки изменяемые, сохраняет ссылки на этим объекты
print(food[0])
food[0] = 'peach'
print(food)
food.append(True)       # append - добавить элемент в конец списка
print(food)
food.extend(['string', 2])  # extend - добавляет список
print(food)
food.remove('peach')    # remove - удаление элемента из списка
print(food)
print('coconut' not in food)    # in если ли элемент в списке или not in
print(food[0:3:2])'''

#Изменяемые и неизменяемые объекты. Кортежи

tuple_ = 1, 3, 5, True, '123'
list = [1, 3, 5, True, '123']
tuple2 = (1, 3, 5)
tuple3 = tuple([1, 3, 5])       # несколько способов создания кортежа
print(tuple_)        # Кортеж, не изменяемый список
print(type(tuple3))
#tuple_[0] = 1
#print(tuple_)
#занимает меньше места в памяти, почти на 25%
print(tuple_.__sizeof__())
print(list.__sizeof__())
tuple4 = ([1, 2], 6) + (1, 3)   # список в кортеже заменить(удалить нельзя) и поддерживает concatenate, можно складывать
print(tuple4)
tuple4[0][0] = 6
print(tuple4)
tuple_ = (1, 2) * 3
print(tuple_)
tuple4[0][0] = ''
print(tuple4)

