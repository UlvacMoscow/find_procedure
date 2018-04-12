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


def last_point(len_output_list, last_sql_file):
    if len_output_list == 1:
        print('Остался один файл с именем', last_sql_file)


def open_filter_list(container_list, word):
    output_list = []
    for sql in container_list:
        with open(os.path.join(os.path.dirname(__file__), migrations, sql), encoding='utf-8') as f:
            if word in f.read():
                output_list.append(sql)
    print('кол-во файлов с этим словом', len(output_list))
    # print('\n'.join(output_list))
    for out in output_list:
        print(out)
    last_point(len(output_list), output_list)
    return output_list

if __name__ == '__main__':
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    migrations_dir = os.path.join(current_dir,migrations)
    print(current_dir)
    print(migrations_dir)
    list_dir = os.listdir(migrations_dir)
    entry_list = []
    list_filter = []

    for sql in list_dir:
        if sql.endswith('.sql'):
            entry_list.append(sql)

    while True:
        word = input('Filter:')
        if not word:
            break
        entry_list = open_filter_list(entry_list, word)






