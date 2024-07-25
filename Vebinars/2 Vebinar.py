def func (*args, **kwargs):
    print(args)
    print(type(kwargs))


func(1,2,3, kwargs=(1,2,3))     # kwargs = принимает словари на вход, нужно сделать переменную именной
a = []
word = 'Hello' if len(a) == 1 else 'World'      # Тернарный оператор, компактный и легко читаемый, работает быстрее возможно. Первое изменение засунули за if (за оператор)
word, word2 = 'Hello', 'Hi' if len(a) == 1 else 'World'     # Несколько значений
print(word)
# || равно этому
if len(a) == 1:
    word = "Hello"
else:
    word = 'World'
