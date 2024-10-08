class Database:                     # класс для хранения данных наших пользователей, логин пароль
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):         # метод для добавления в словарь данных пользователей
        self.data[username] = password

class User:
    '''
    Класс пользователя содержащий атрибуты: логин, пароль
    '''
    def __init__(self, username, password, password_confirm):      # записываем логин, пароль и просим повторить пароль, если они совпадают записываем пароль
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход \n2 - Регистрация\n'))        # зациклили с помощью while для входа, но сначало надо зарегаться
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:                  # проверяем если ли такой логин(ключ) в базе
                if password == database.data[login]:    # проверка пароля
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль.')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),        # передаём данные в класс, с помощью := моржа
                        password2 := input('Повторите пароль'))
            if password != password2:
                print('Пароли не совпадают, попробуйте ещё раз.')
                continue
            database.add_user(user.username, user.password)
