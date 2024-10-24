class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
      print(first)
      print(second)
      print(third)


ex = Example('data', second=25, third=3.14)

users = [['vasya_pupkin', 'F8098FM8fjm9jmi', 55]]
for  i in users:
    if i[0] == 'vasya_pupkin':
        print(1)



a = [1, 2, 3]
print(sum(a))
