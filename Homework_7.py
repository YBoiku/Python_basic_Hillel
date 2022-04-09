################# 1 #################
# number = 102350120320056
# result = str(number).count('0')
#
# print(result)
################# 2 #################
# number = 1002000
# len_orig_number = len(str(number)[::-1])
# len_rev_number = len(str(int(str(number)[::-1])))
# count_zero_back = len_orig_number - len_rev_number
# print(count_zero_back)
# count_zero_back = len(str(number)[::-1]) - len(str(int(str(number)[::-1])))
################# 3 #################
# my_list_1 = [1, 2, 3, 4, 5, 7, "house", 8, 9, 15, "qwerty", "apple"]
# my_list_2 = [1, 2, 3, 4, 5, 156, "cat", "dog"]
# my_result = []
#
# my_range_1 = my_list_1[1::2]
# my_range_2 = my_list_2[0::2]
#
# for index in my_range_1:
#     my_result.append(index)
# for index1 in my_range_2:
#     my_result.append(index1)
# print(my_result)
# Код работает, но уверен можно легче написать, но другого решения найти не смог. Сможете подсказать с правильным?
################# 4 #################


# my_list = [1, 2, 3, 4]
# new_list = []
# range_list = my_list[1:]
#
# for create_list in range_list:
#     new_list.append(create_list)
# new_list.append(my_list[0])
# print(new_list)


################# 5 #################
# my_list = [1, 2, 3, 4]
# my_list += [my_list.pop(0)]
# print(my_list)
################# 6 #################
# some_string = "43 больше чем 34 но меньше чем 56"
# some_string_1 = some_string.split()
# count = []
# for numbers in some_string_1:
#     if numbers.isdigit() == True:
#         count.append(int(numbers))
# result = sum(count)
# print(result)
################# 7 #################
# my_str = "Carpe diem - memento mori"
# my_str_l = my_str.lower()
# l_limit = "e"
# r_limit = "o"
# # ff_l_split = my_str_l.find(f'{l_limit}')
# # l_split = my_str[ff_l_split + 1::]
# # rev_split = l_split[::-1]
# # ff_r_split = rev_split.find(f'{r_limit}')
# # r_split = rev_split[ff_r_split + 1::]
# # end_revers = r_split[::-1]
# # print(end_revers)
#
# left_split = my_str_l[my_str_l.find(f"{l_limit}") + 1:]
# rev_split = left_split[::-1]
# right_split = rev_split[rev_split.find(f"{r_limit}") + 1:]
# end_revers = right_split[::-1]
# print(end_revers)
################# 8 #################
# my_str = 'qwertyu'
# list_for_str = []
# if len(my_str) % 2 != 0:
#     my_str += '_'
# else:
#     pass
# coefficient = 2
# for two_symbol in range(0, len(my_str), coefficient):
#     new_str = my_str[two_symbol:two_symbol + coefficient]
#     list_for_str.append(new_str)
#     if two_symbol == 1:
#         list_for_str.append("_")
# print(list_for_str)
################# 9 #################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# some_list = [2, 4, 1, 5, 3, 9, 0, 7]
# list_s = []
#
# for x in some_list:
#     if some_list.index(x) == 0 or some_list.index(x) == len(some_list) - 1:
#         pass
#     elif x > some_list[(some_list.index(x))-1] + some_list[(some_list.index(x))+1]:
#         list_s.append(x)
#
# print(list_s)
# Это единственный способ который я нашел и работал у меня, единственное у него есть нюанс
# если использовать список с повторяющимеся элементами, то они оба будет выводится, в не зависимости от равенства
# как пример вот список: some_list = [2, 4, 1, 5, 3, 9, 0, 7, 9, 72]
################# 10 #################
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for str_number in my_list:
#     if type(str_number) is str:
#         new_list.append(str_number)
# print(new_list)
################# 11 #################
# my_list = [1, 22, 3, 5, 5, 33, 44, 44]
# new_list = []
# for some_list in set(my_list):
#     new_list.append(some_list)
# print(new_list)
################# 12 #################
# my_list_1 = [1, 3, 5, 33, 44]
# my_list_2 = [22, 3, 7, 10, 44]
# my_set_1 = set(my_list_1)
# my_set_2 = set(my_list_2)
# new_set = my_set_1.intersection(my_set_2)
# new_list = list(new_set)
# print(new_set)
################# 13 #################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# my_string_1 = "aaaasdf1"
# my_string_2 = "asdfff2"
# some1 = []
# some2 = []
# for symbol1 in set(my_string_1):
#     some1.append(symbol1)
# print(some1)
# for symbol2 in set(my_string_2):
#     some2.append(symbol2)
# print(some2)
