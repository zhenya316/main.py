class Human:
    def __init__(self, name, age):           # __init__ - метод который работает 1 раз нужен для инцилизация класса
        self.name = name                # self -
        self.age = age                  # атрибуты, переменные внутри класса, при создание передаём значение
        self.say_info()                 # вызвали метод внутри класса
    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')                # Метод, собственная структура данных, собственный тип, с собственными характеристиками и способностями

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')


den = Human('Denis', 22)
max_ = Human('Max', 22)

print(max_.name, max_.age)
max_.age = 23                           # Мы можем как создавать атрибуты, так и изменять уже существующие
print(max_.name, max_.age)
print(den.name, den.age)
den.say_info()
max_.birthday()

# Атрибуты — это переменные внутри класса. Методы — это функции внутри класса. По-другому можно сказать, что атрибуты — это характеристики,
# то есть какие-то уникальные черты наших объектов, а методы — это способности, то есть то, что умеет делать наш объект.
# Видим здесь self, он является указателем на самого себя, то есть указателем на объект
