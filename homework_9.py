from random import choice, randint, random, sample
from string import ascii_lowercase


###################### 1 #######################
def for_reverse_odd_string(original_strings_list):
    reversed_string = []
    for index_string, string_value in enumerate(original_strings_list):
        if index_string % 2 != 0:
            reversed_string.append(original_strings_list[index_string])
        else:
            reversed_company = original_strings_list[index_string][::-1]
            reversed_string.append(reversed_company)
    return reversed_string


my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt", "Luxoft", "Genesis"]
new_list = for_reverse_odd_string(my_list)


###################### 2 #######################
def filter_first_a(original_strings_list):
    filter_strings_list = []
    for each_word in original_strings_list:
        if each_word[0].lower() == "a":
            filter_strings_list.append(each_word)
    return filter_strings_list


my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt", "Luxoft", "Genesis"]
new_list = filter_first_a(my_list)


###################### 3 #######################
def filter_letter_a(original_strings_list):
    filter_string = []
    for each_word in original_strings_list:
        if "a" in each_word.lower():
            filter_string.append(each_word)
    return filter_string


my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt", "Luxoft", "Genesis"]
new_list = filter_letter_a(my_list)


###################### 4 #######################
def filter_for_str(some_list):
    list_result_filter = []
    for str_number in some_list:
        if type(str_number) is str:
            list_result_filter.append(str_number)
    return list_result_filter


my_list = [1, 2, 3, "11", "22", 33]
new_list = filter_for_str(my_list)


###################### 5 #######################
def unique_symbol_in_string(some_list):
    list_result_filter = []
    for some_symbols in set(some_list):
        if some_list.count(some_symbols) == 1:
            list_result_filter.append(some_symbols)
    return list_result_filter


my_list = [1, 22, 3, 5, 5, 33, 44, 44]
new_list = unique_symbol_in_string(my_list)


###################### 6 #######################
def intersection_list_filter(list_1, list_2):
    list_1 = set(list_1)
    list_2 = set(list_2)
    new_set = list_1.intersection(list_2)
    return list(new_set)


my_list_1 = [1, 3, 5, 33, 44]
my_list_2 = [22, 3, 7, 10, 44]
new_list = (intersection_list_filter(my_list_1, my_list_2))


###################### 7 #######################
def unique_common_sym_two_str(string_1, string_2):
    unique_common_sym = []
    for some_sym in set(string_1):
        if string_1.count(some_sym) == 1 and string_2.count(some_sym) == 1:
            unique_common_sym.append(some_sym)
    return unique_common_sym


my_string_1 = "aaaasdf1"
my_string_2 = "asdfff2"
new_list_1 = unique_common_sym_two_str(my_string_1, my_string_2)


###################### 8 #######################
def create_email(user_domain, user_name):
    random_name = choice(user_name)
    random_numbers_1 = str(randint(100, 999))
    random_numbers_2 = "".join(sample(list(set(ascii_lowercase)), randint(5, 7)))
    random_domain = choice(user_domain)
    random_email = f"{random_name}.{random_numbers_1}@{random_numbers_2}.{random_domain}"
    return random_email


name = ["pink_killer", "grinch", "konstantine", "nibulon777"]
domain = ["ua", "biz", "org", "coop", "eus", "edu"]
new_email = create_email(domain, name)
