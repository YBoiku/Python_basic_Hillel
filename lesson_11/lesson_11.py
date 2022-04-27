# Параметры по умолчанию
# позиционные и именнованые аргументы
# Типы переменных | анотация типов
# Импорт функций

import os
from utils.files import read_txt_file_as_str

path = "../All_homework/Homework text"
list_dir = os.listdir(path)
# print(list_dir)

filename = 'names.txt'
base_dir = ''
data = read_txt_file_as_str(f'{path}/{base_dir}/{filename}')
# data = read_txt_file_as_str(os.path.join(path, filename))
# print(data)

for filename in list_dir:
    filepath = os.path.join(path, filename)
    if os.path.isdir(filepath):
        print(filepath)


# from utils.files import read_txt_file_as_str, DEBUG_MOD
#
# data = read_txt_file_as_str('test.txt')
# print(f'{__name__=}')
# print(data)
# print(DEBUG_MOD)

# def read_txt_file(filename: str = 'test.txt', debug_mod: bool = True) -> str:
#     with open(filename, 'r', encoding='utf-8') as my_file:
#         data = my_file.read()
#     if debug_mod:
#         print(data)
#     return data
#
#
# data = read_txt_file('test.txt', True)

##################################################################################
# def get_args(*args, **kwargs):
#     for arg_value in args:
#         print(arg_value)
#     for kwargs_value in kwargs:
#         print(kwargs_value, kwargs[kwargs_value])
#
# get_args(1, 2, 'qwe', name='John', age=12)

# from random import choice, randint
# from string import ascii_lowercase as alphabet
#
# DEBUG_MOD = True
#
#
# def create_email(domains, names, debug_mod=DEBUG_MOD):
#     name = choice(names)
#     number = randint(100, 999)
#     some_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
#     domain = choice(domains)
#     e_mail = f"{name}.{number}@{some_str}.{domain}"
#     if debug_mod:
#         print(e_mail)
#     return e_mail
#
#
# names_list = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(names=names_list, domains=domains)
#
#
# def read_txt_file(filename='test.txt', debug_mod=DEBUG_MOD):
#     with open(filename, 'r', encoding='utf-8') as my_file:
#         data = my_file.read()
#     if debug_mod:
#         print(data)
#     return data
#
#
# data = read_txt_file()
