print(5)
print(type(1))   #определение типа данный текст = str()-string, целые числа = int-integer, дробные числа = float(). Типов данных много, деляться они на изменяемые и не изменяемые
print(5//5)           # / - дробное деление = float ()  // - целочисленное деление
print(5%4)            # % - получение остатка после деления, для определения чётности например и др.
print(5 ** 2)         # ** - возведение в степень
print('Hello world')  # str - в кавычках
print('hello' + ' world')   # concatenate сложение строк, можно только складывать строки
print(True, False)  # bool-boolean - логический тип данных, правда или ложь, это тип данных имеет только 2 переменных
print(type(True), type(False))  # Нужны для флагов или сигналов, if elif else, в программе и не только
print(5 > 6, 5 < 6)  # False
print(5 > 6)    # >, <, ==(равны?), >=, <=, !=(не равны?)
print(5 != 6 and 5 < 10 or 1 >= 1, not 1>2)  # and, or, not, if, elif, else

print(type(str(1)), type(int('1')), type(float(1)), type(bool(1)))  # перевод из одного типов данных в другой, число не может быть str и наоборот
