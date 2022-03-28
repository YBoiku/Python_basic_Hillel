# debuger
# for
# str methods
###################### for ######################

# my_str = "qwerty123456"

# for symbol in my_str:
#     print(symbol)

# for symbol in my_str[:6]:
#     print(symbol)

# for index in range(len(my_str)):
#     print(index, my_str[index])

# for index, symbol in enumerate(my_str):
    # print(index, symbol)

# for item in enumerate(my_str):
#     print(item)

###################### str methods #####################
# my_str = "qwerty123456"
# my_str = "qwerty"
# my_str = "Qwe.rtY"
# my_str = "123"
# my_str = "My name is John, i'm 40"

# my_str_len = len(my_str)
# print(my_str_len)
# print(my_str.islower())

# for symbol in my_str:
#     if not symbol.isupper():
#         print(symbol)

# for symbol in my_str:
#     if symbol in 'eyuioa':
#         print(symbol)

# for symbol in my_str:
#     if symbol.isalpha() and symbol.islower() and symbol not in 'eyuioa':
#         print(symbol)

# result = my_str.rfind('m')
# print(result)

filename = "image_png_123.png"
f_name = filename[::-1].replace('gnp', 'gpj', 1)
filename = f_name[::-1]
# filename = filename.replace('png', 'jpg', 1)
print(filename)

# my_str = "My name is Anna, I'm 40. It is dog."

# for symbol in my_str:
#     if symbol.lower() in 'eyuioa':
#         print(symbol)

# print(my_str.lower().count('a'))

# result = ""
# for symbol in my_str:
#     if symbol.isalpha() and symbol.islower() and symbol not in 'eyuioa':
#         result += symbol
# print(result)