
#############################################################
# none_value = None
# print(none_value, type(none_value))

# value = 123
# id_value = id(value)
# print(id_value)
# print_value = print(value)
# print(print_value)
#############################################################
# value_1 = True
# value_2 = False
# print(type(value_1), type(value_2))

# bool_value = 4 > 2 # >, <, >=, <=, ==, !=
# bool_value = "qwe" in "qwerty"

# print(bool_value)
#############################################################
# value_int = 12
# value_float = 3.14
# result = value_int + value_float
# print(result)

# value_int = 1
#
# value_float = float(value_int) # int -> float
# value_str = str(value_int) # int -> str
# value_bool = bool(value_int) # int -> bool !!! True всегда больше 0
#
# print(type(value_str), type(value_float), value_bool)

#############################################################
# value_float = 3.99999999999
#
# value_int = int(value_float) # float -> int !!! отрезание всего после точки
# value_str = str(value_float) # float -> str
# value_bool = bool(value_float) # float -> bool !!! True всегда больше only 0.0
#
# print(value_int, value_float, value_bool)
#############################################################

# value_str = "10"
#
# value_int = int(value_str) # float -> int
# value_float = float(value_str) # float -> str # утиная типизация
# value_bool = bool(value_str) # float -> bool True всегда кроме ""
#
# print(value_int, value_float, value_bool)

########################### оператор if ##################################

# value = 10
# if условие:
    # блок если Да
# elif условие_2:
    # блок если Да
# else:
    # блок если НЕТ


# if value < 0:
#     print(f"{value} меньше чем 0")
# elif 0 <= value < 100:
#     print(f"{value} больше 0, но меньше 10")
# elif 10 <= value < 100:
#     print(f"{value} больше 10, но меньше 100")
# else:
#     print(f"{value}  Больше или равно 100")

########################### input ##################################

# input_value = input("Введи целое число: ")
# int_value = int(input_value)
# print(int_value, type(int_value))

# int_value = int(input("Введи целое число: "))
# print(int_value, type(int_value))
########################### обработка ошибок ##################################

# input_value = input("Введи целое число: ")
# try:
#     int_value = int(input_value)
#     print(int_value, type(int_value))
# except ValueError:
#     print("Это не целое число")
# except ZeroDivisionError:
#     print("На ноль дилить нельзя")
#####################################################################

input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
value_1 = input("Введи первое число: ")
value_2 = input("Введи второе число: ")