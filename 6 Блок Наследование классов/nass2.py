class Human:

    head = True
    _legs = True            # _ для локального использования, импортировать класс с _ не получиться
    __arms = True           # двойное __ нужно для неизменяемой переменной, её нельзя поменять в дочерних классах. Создлаёт уникальное имя
    def say_hello(self):
        print('Здравствуйте')
    def about(self):            # self - подставляеться обьект класса _Human, при вызове в дочерних классах
        print(self.head)
        print(self._legs)
        print(self.__arms)




class Student(Human):
    #arms = False
    pass
    # def about(self):
    #     print('я студент')



class Teacher(Human):
    pass

human = Human()
human.about()

student = Student()
student.about()

print(dir(Human))
print(dir(Student))     # два разных arms


print(student._Human__arms)