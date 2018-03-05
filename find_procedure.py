# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
migrations_dir = os.path.join(current_dir,migrations)

if __name__ == '__main__':
    print(current_dir)
    print(migrations_dir)

    list_dir = os.listdir(migrations_dir)
    list_dir_sql = []
    list_filter = []


    def last_point(a, b):
        if a == 1:
            print(b)


    def open_filter_list(list_1, list_2, filter):
        for sql in list_1:
            with open(os.path.join(os.path.dirname(__file__), migrations, sql), encoding='utf-8') as f:
                if filter in f.read():
                    list_2.append(sql)
        print(len(list_2))
        list_1.clear()
        last_point(len(list_2), list_2)


    for sql in list_dir:
        if sql.endswith('.sql'):
            list_dir_sql.append(sql)


    def sql_filter(list, list_filter, filter):
        if len(list) > 0:
            open_filter_list(list, list_filter, filter)
        else:
            open_filter_list(list_filter, list, filter)


    while True:
        filter = input('Filter:')
        if not filter:
            break
        sql_filter(list_dir_sql, list_filter, filter)
    pass




