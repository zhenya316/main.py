class Human:

    head = True
    def say_hello(self):
        print('Здравствуйте')
    # def __init__(self):
    #    self.about()




class Student(Human):
    # head = False, вначале смотрим в своей области видимости класса, если нет атрибута, обращаемся к родительскому
    def about(self):
        print('я студент')



class Teacher(Human):
    pass



# human = Human()
student = Student()  # в self __init__ подставился класс Student, вызвал метод about из класса Human
print(Student.head)  # получили доступ к родительскому атрибуту через дочерний класс
student.say_hello()
Teacher.say_hello()


# Наследование нужно чтобы не дублировать код, вначале смотрим атрибуты и методы дочернего класса, если нет переходим в родительский класс