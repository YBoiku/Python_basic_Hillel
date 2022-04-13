from random import choice, randint, random, sample
from string import ascii_lowercase


###################### 1 #######################
def for_reverse_string(original_string):
    reversed_string = []
    for index_companies_list, companies_list in enumerate(original_string):
        if index_companies_list % 2 != 0:
            reversed_string.append(original_string[index_companies_list])
        else:
            reversed_company = original_string[index_companies_list][::-1]
            reversed_string.append(reversed_company)
    return reversed_string


###################### 2 #######################
def filter_first_a(some_string):
    new_list = []
    for each_word in some_string:
        if each_word[0].lower() == "a":
            new_list.append(each_word)
    return new_list


###################### 3 #######################
def filter_letter_a(some_string):
    filter_string = []
    for each_word in some_string:
        if "a" in each_word.lower():
            filter_string.append(each_word)
    return filter_string


###################### 4 #######################
def filter_for_str(some_list):
    new_list = []
    for str_number in some_list:
        if type(str_number) is str:
            new_list.append(str_number)
    return new_list


###################### 5 #######################
def filter_set(some_list):
    new_list = []
    for some_symbols in set(some_list):
        if some_list.count(some_symbols) == 1:
            new_list.append(some_symbols)
    return new_list


###################### 6 #######################
def filter_intersection(list_1, list_2):
    list_1 = set(list_1)
    list_2 = set(list_2)
    new_set = list_1.intersection(list_2)
    return list(new_set)


###################### 7 #######################
def set_two_string(string_1, string_2):
    new_list = []
    for some_sym in set(string_1):
        if string_1.count(some_sym) == 1 and string_2.count(some_sym) == 1:
            new_list.append(some_sym)
    return new_list


###################### 8 #######################
def create_email(user_domain, user_name):
    random_names = choice(user_name)
    random_numbers_1 = str(randint(100, 999))
    random_numbers_2 = "".join(sample(list(set(ascii_lowercase)), randint(5, 7)))
    random_domains = choice(user_domain)
    random_email = f"{random_names}.{random_numbers_1}@{random_numbers_2}.{random_domains}"
    return random_email
