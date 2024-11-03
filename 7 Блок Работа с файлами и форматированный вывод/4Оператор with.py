import re
import io
from pprint import pprint

# файл схож со списком по свойствам
b = []
name = 'testovii3.txt'
with open(name, encoding='utf-8') as file:      # with сам закрывает файл в конце выполнения программы
    for line in file:
        s = re.sub('[;|.|,|]', '', line)
        m = s.replace('', '')
        a = m.lower().split()
        b += a
        print(b)

a = 'sadsadas.,;'
s = re.sub('[;|.|,]', '', a)
print(s)
a = ['a',2,3]
for i in range(len(a)):
    print(i)
    print(a[i])