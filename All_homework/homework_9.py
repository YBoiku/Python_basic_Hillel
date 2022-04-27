from random import choice, randint, random, sample
from string import ascii_lowercase


###################### 1 #######################
def reverse_odd_string_in_list(original_strings_list):
    reversed_string = []
    for company_index, company_name in enumerate(original_strings_list):
        if company_index % 2 != 0:
            reversed_string.append(original_strings_list[company_index])
        else:
            reversed_company = original_strings_list[company_index][::-1]
            reversed_string.append(reversed_company)
    return reversed_string


###################### 2 #######################
def find_first_letter_a_in_companies_name_list(original_strings_list):
    company_with_first_letter_a = []
    for each_word in original_strings_list:
        if each_word[0].lower() == "a":
            company_with_first_letter_a.append(each_word)
    return company_with_first_letter_a


###################### 3 #######################
def find_letter_a_in_companies_name_list(original_strings_list):
    company_with_letter_a = []
    for each_word in original_strings_list:
        if "a" in each_word.lower():
            company_with_letter_a.append(each_word)
    return company_with_letter_a


my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt", "Luxoft", "Genesis"]
new_list = reverse_odd_string_in_list(my_list)


# new_list = find_first_letter_a_in_companies_name_list(my_list)
# new_list = find_letter_a_in_companies_name_list(my_list)


#######################################################################################################################
###################### 4 #######################
def search_for_a_str_in_list(some_list):
    result_search_a_str = []
    for str_number in some_list:
        if type(str_number) is str:
            result_search_a_str.append(str_number)
    return result_search_a_str


my_list = [1, 2, 3, "11", "22", 33]
new_list = search_for_a_str_in_list(my_list)


###################### 5 #######################
def search_for_a_unique_sym_in_list(some_list):
    result_search_a_unique_sym = []
    for some_symbol in set(some_list):
        if some_list.count(some_symbol) == 1:
            result_search_a_unique_sym.append(some_symbol)
    return result_search_a_unique_sym


my_list = [1, 22, 3, 5, 5, 33, 44, 44]
new_list = search_for_a_unique_sym_in_list(my_list)


###################### 6 #######################
def search_for_a_sym_intersection_in_list(list_1, list_2):
    list_1 = set(list_1)
    list_2 = set(list_2)
    sym_intersection = list_1.intersection(list_2)
    return list(sym_intersection)


my_list_1 = [1, 3, 5, 33, 44]
my_list_2 = [22, 3, 7, 10, 44]
new_list = search_for_a_sym_intersection_in_list(my_list_1, my_list_2)


###################### 7 #######################
def search_for_a_sym_intersection_in_str(string_1, string_2):
    sym_intersection_list = []
    for some_sym in set(string_1):
        if string_1.count(some_sym) == 1 and string_2.count(some_sym) == 1:
            sym_intersection_list.append(some_sym)
    return sym_intersection_list


my_string_1 = "aaaasdf1"
my_string_2 = "asdfff2"
new_list_1 = search_for_a_sym_intersection_in_str(my_string_1, my_string_2)


###################### 8 #######################
def create_email(user_domain, user_name):
    random_user_name = choice(user_name)
    random_numbers = str(randint(100, 999))
    random_letters = "".join(sample(list(set(ascii_lowercase)), randint(5, 7)))
    random_domain = choice(user_domain)
    random_email = f"{random_user_name}.{random_numbers}@{random_letters}.{random_domain}"
    return random_email


names = ["pink_killer", "grinch", "konstantine", "nibulon777"]
domains = ["ua", "biz", "org", "coop", "eus", "edu"]
new_email = create_email(domains, names)
