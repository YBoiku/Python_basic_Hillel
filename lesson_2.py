# value = 3
# new_value = 5.1
# my_string = "Hello!!!"

# print(value, new_value, my_string)

# type - функция для получение типа объектов
# int - тип целых чисел <class 'int'>

# print(type(value))

# val_1 = -23
# val_2 = 10

# result = val_1 + val_2
# result = val_1 * val_2
# result = val_1 ** val_2
# result = val_1 - val_2
# result = val_1 / val_2
# result = val_1 // val_2
# result = val_1 % val_2
#
# print(result, type(result))

###################################################################
# float

# val_1 = 23.2
# val_2 = 10.4

# result = val_1 + val_2
# result = val_1 * val_2
# result = val_1 - val_2
# result = val_1 / val_2
# result = val_1 // val_2 # не рекомендую
# result = val_1 % val_2 # не рекомендую
#
# print(result, type(result))

###################################################################

# value_int = 3
# value_float = 4.3
# value_int = value_float
# value_float = 5
# id() - функция получения id  объекта

# print(id(value_int), id(value_float))
###################################################################

# str - строковый тип данных

# my_str = "New string"
# my_str = 'New string'
# my_str = '''New string'''
# my_str = """New string"""
# my_str = 'FC "Arsenal"'
# my_str = "I'm a boy"
# print(my_str, type(my_str))

# new_str = 'My\tname\this\tVova'
# new_str = r'My\tname\this\tVova' # raw string

# value = 3
# f_str = f"My value is {value}"
# f_str = f"{value=}"
# print(f_str)

# my_int = 5
# my_float = 3.14
# my_str = "New string"
# new_str = "!!!"
# result = my_int + my_float
# print(result)

folder = "images"
filename = "photo_1"
ext = "png"
# path = folder + "/" + filename
path = f"{folder}/{filename}.{ext}"
print(path)

###################################################################



