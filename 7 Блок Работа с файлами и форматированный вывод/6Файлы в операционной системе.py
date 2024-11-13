import os

print('Текущая директория', os.getcwd())        # getcwd - показывает в какой сейчас директории
if os.path.exists('second'):                    # если есть такая директория, то выведет её, иначе создаст её
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория', os.getcwd())
#os.makedirs(r'third\fourth')       # makedirs - создать директорию, через \ можно сделать вложенную директорию, r'-нужно для при\ разметки
print(os.listdir())
for i in os.walk('.'):  # обходит всю директорию. выводит список вложенных директорий, [] - показывает глубины вложенности директории
    print(i)
os.chdir(r'C:\Проекты на Питоне\Обучение\7 Блок Работа с файлами и форматированный вывод')
print('Текущая директория', os.getcwd())
print(os.listdir())     # выводит список файлов в директории в листе
file = [f for f in os.listdir() if os.path.isfile(f)]   # генератор списка с условием что добавляем только файлы
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)
os.startfile(file[-1])  # запустили один из файлов, в блокноте отдельно вывелся
print(os.stat(file[-1]).st_size)    # stat вернёт информациию о файле, или можно получить интересующий нас файл
os.system('pip install random2') # system - запустили в терминале
print(os.stat(file[-1]))
# библиотека os - очень объёмная и имеет много интересных возможностей, перемещение, создание, изменение файла и др.
