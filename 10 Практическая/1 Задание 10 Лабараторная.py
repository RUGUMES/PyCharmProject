print('Кодовый замок')
password = '4590'
while True:
    password_user = input('Введите пароль: ')
    if password == password_user:
        print('Доступ разрешён.')
        break
    else:
        print('Ошибка. Попробуйте еще раз.')

