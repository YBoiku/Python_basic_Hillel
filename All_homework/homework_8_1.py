######################## 1 ########################
my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt"]
new_my_list = []
for index_companies_list, companies_list in enumerate(my_list):
    if index_companies_list % 2 != 0:
        new_my_list.append(my_list[index_companies_list])
    else:
        reversed_company = my_list[index_companies_list][::-1]
        new_my_list.append(reversed_company)
######################## 2 ########################
my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt", "Luxoft", "Genesis"]
new_my_list = []
for each_word in my_list:
    if each_word[0].lower() == "a":
        new_my_list.append(each_word)
######################## 3 ########################
my_list = ["N-iX", "AUTO DOC", "EPAM", "Sigma Software", "Ciklum", "DataArt", "Luxoft", "Genesis"]
new_my_list = []
for each_word in my_list:
    for symbol_a in set(each_word.lower()):
        if symbol_a == "a":
            new_my_list.append(each_word)
######################## 4 ########################
persons = [{"name": "John", "age": 40},
           {"name": "Kira", "age": 19},
           {"name": "Ivan", "age": 21},
           {"name": "Konstantine", "age": 37},
           {"name": "Alex", "age": 45},
           {"name": "Natali", "age": 19},
           {"name": "Konstantine", "age": 37},
           ]
############# a ##############
young_man = []
all_age = []
for some_age in persons:
    all_age.append(some_age["age"])
for min_age in persons:
    if min(all_age) == min_age["age"]:
        young_man.append(min_age["name"])
############# b ##############
long_name = []
all_name = []
for some_name in persons:
    all_name.append(len(some_name["name"]))
for some_name in persons:
    if len(some_name["name"]) == max(all_name):
        long_name.append(some_name["name"])
############# c ##############
average_age = []
for all_age in persons:
    average_age.append(all_age["age"])
average_price = sum(average_age) / len(average_age)
######################## 5 ########################
my_dict_1 = {"name": "Josh", "city": "New York", "boroughs": "Bronx", "age": 28, "zip": 10001}
my_dict_2 = {"city": "New York", "mayor": "Eric Adams", "age": 61, "zip": 10001}
############# a ##############
general_keys = []
for key, value in my_dict_1.items():
    if key in my_dict_2:
        general_keys.append(key)
############# b ##############
different_keys = []
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        different_keys.append(key)
############# c ##############
different_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        different_dict.update({key: value})
############# d ##############
all_dict = {}
for key_1, value_1 in my_dict_1.items():
    for key_2, value_2 in my_dict_2.items():
        if key_1 not in my_dict_2:
            all_dict.update({key_1: value_1})
        elif key_2 not in my_dict_1:
            all_dict.update({key_2: value_2})
        else:
            all_dict.update({key_1: [value_1, value_2]})
