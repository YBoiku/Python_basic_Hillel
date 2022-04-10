# распаковка ротежей и списков

# my_tuple = (1, 2, "OK", "test")
# value_1, value_2, my_str = my_tuple
# print(value_2)
############################################################
value_1 = 2
value_2 = 4
# value_2, value_1 = value_1, value_2
# print(value_1, value_2)
#
# Объяснение процесса обмена значениий в переменных
# tmp = value_1, value_2 # создает кортеж
# print(tmp)
# value_2, value_1 = tmp
# print(value_1,value_2)
############################################################
# value_1, value_2, _ = my_tuple
# print(value_1, value_2)

# value_1, value_2, *_, last_value = my_tuple
# print(last_value)

# print(my_tuple)
# print(*my_tuple)
############################################################

##################### Словари и методы словарей #####################

# my_dict = {"key": "value"} # ключ - любой НЕИЗМЕНЯЕМЫЙ объект, значение - любой объект
# print(my_dict, type(my_dict))

address = {"city": "Dnipro",
           "street": "Polya",
           "zip": 49000,
           }
#
# person = {"name": "John",
#           "age": 24,
#           "job": "president",
#           "adress": address,
#           }
# print(person)
# print(person["adress"]["city"])

# test_dict = {1: "test1", 2.3: "test2"}
# print(test_dict)

# from random import randint
#
# cube_dict = {1: "thi is 1",
#              2: "thi is 2",
#              3: "thi is 3",
#              4: "thi is 4",
#              5: "thi is 5",
#              0: "thi is 6",
#              }
# value = randint(1, 100)
# my_result = cube_dict[value % 6]
# print(value, my_result)

# test_dict = dict()
# test_dict["new_key"] = 100
# my_dict = {"test": "value", "test_2": 2}
# test_dict.update(my_dict)
#
# # get_value = test_dict["key"]
# get_value = test_dict.get("key", -1)
# pop_value = test_dict.pop("test")
#
# print(pop_value, test_dict, get_value)

# address["district"] = "center"
# address["Zip"] = 49001
# print(address)
############################################################
# key = "key"
# if key in address: # in смотрит в ключи словаря!!!
#     get_value = address[key]
#     print(get_value)
# else:
#     address[key] = None

# print(address.keys())
#
# for key in address.keys():
#     print(key, address[key])

# print(address.values())
# for value in address.values():
#     print(value)

# items = address.items()
# print(items)
# for key, value in address.items():
#     print(value, key)
############################################################
ascii_dict = {}
# for key in range(50, 60):
#     ascii_dict[key] = chr(key)
#
# ascii_dict = {key: chr(key) for key in range(50, 60)}
# print(ascii_dict)

# ascii_dict_values = {}
# for key, value in ascii_dict.items():
#     ascii_dict_values[value] = key
#
# print(ascii_dict_values)

price_list = [{"product": "MacBook", "price": 32000, "brand": "Apple"},
              {"product": "Zephyrus", "price": 46000, "brand": "Asus"},
              {"product": "HP", "price": 17000, "brand": "HP"},
              ]

prices = []
for notebook in price_list:
    prices.append(notebook["price"])

average_price = sum(prices) / len(prices)
print(average_price)
