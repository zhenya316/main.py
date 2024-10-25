class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)     # супер обращается к классу правее его - StudentGroup
        super().about()
    def info(self):
        print(f'Привет меня зовут {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учиться в группе {self.group}')
class Student(Human, StudentGroup):         # можно наследовать сколько угодно
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()

#human = Human('Женя')
#print(human.name)
student = Student("Макс", "УрБАН", "Питоны")
#student.about()
print(Human.mro())
print(Student.mro())    # кто левее тот главнее, super() - обращается слева направо

# mro - полезный метод для понимания иерархии наследования классов,
#Super() - это функция, которая позволяет вызывать методы родительского класса в дочернем классе. Она используется чтобы избежать дублирования кода и улучшить его читаемость.