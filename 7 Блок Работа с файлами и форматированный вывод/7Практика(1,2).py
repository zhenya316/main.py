import tkinter      # библиотека для вызова окна, создания кнопок
from tkinter import filedialog  # для вызова диалогового окна
import os

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title="Выберите файл",
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename         # Нашли файл, подставили его в text в кнопке
    os.startfile(filename)                              # Открыли выбранный файл

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x350')
window.configure(bg='green')
window.resizable(False, False)                          # блокировка изменений для пользователя
text = tkinter.Label(window, text='Файл:', height=5, width=65, bg='silver', fg='blue')      # bg(background) - цвет фона, fg(foreground) - цвет текста
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=40, height=5, text='Выбрать файл', background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2)
button_menu = tkinter.Button(window, width=40, height=10, text='Меню \n'
                                                              'Выберите файл который хотите открыть\n'
                                                              'Путь к файлу будет сверху\n'
                                                              'О программер:\n'
                                                              'Автор - Женя, версия - 0.1', background='silver', foreground='blue',
                            )
button_menu.grid(column=1, row=3)
window.mainloop()

# Добавить меню к этому блокноту, чтобы был пункт инфо в котором будет написано как работать с блокнотом и
# пункт о программе, в котором будет написано имя автора и версия программы