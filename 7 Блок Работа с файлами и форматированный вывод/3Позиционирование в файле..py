import io
from pprint import pprint

# файл схож со списком по свойствам

name = 'testovii3.txt'
file = open(name, 'r', encoding='utf-8')    # encoding='utf-8' - декодировние при чтении файла
print(file.writable())      # можно ли записать файл, при чтении нет
print(file.readable())      # можно ли прочитать файл
print(file.seekable())      # можно ли переместить курсор
print(file.closed)          # закрыт ли файл
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()