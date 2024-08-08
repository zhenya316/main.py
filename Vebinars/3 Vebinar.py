#! Для создания функции из кода. Выделяем код ПКМ>Refactor>Extract Method
n = 0
b = {(2, 'Urban', ('Urban2', 35))}
print(type(b))
for i in b:
    if isinstance(i, int) or isinstance(i, float):
        n += int(i)
    elif isinstance(i, str):
        n += len(i)
print(n)

# Результат - Extract Method
#               ||
def method_name():
    n = 0
    b = {(2, 'Urban', ('Urban2', 35))}
    print(type(b))
    for i in b:
        if isinstance(i, int) or isinstance(i, float):
            n += int(i)
        elif isinstance(i, str):
            n += len(i)
    print(n)


method_name()

