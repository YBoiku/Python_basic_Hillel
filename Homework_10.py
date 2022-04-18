######################## 1 ########################
def list_of_domains_name_from_file(path_and_filename):
    with open(path_and_filename, 'r') as my_file:
        all_domains = my_file.read()
    domains_names = []
    for each_data_line in all_domains.split('\n'):
        if each_data_line[0] == '.':
            domains_names.append(each_data_line.split('.')[1])
    with open(path_and_filename, 'w') as new_txt_file:
        new_txt_file.write(all_domains)
    return domains_names


list_of_domains_names = list_of_domains_name_from_file('Homework text/domains.txt')


######################## 2 ########################
def list_of_last_names_from_file(path_and_filename):
    with open(path_and_filename, 'r') as my_file:
        all_information_from_file = my_file.read()
    last_names = []
    for data_line in all_information_from_file.split('\n'):
        if data_line:
            each_data_line = data_line.split('\t')
            last_names.append(each_data_line[1])
    with open(path_and_filename, 'w') as new_txt_file:
        new_txt_file.write(all_information_from_file)
    return last_names


last_names_in_file = list_of_last_names_from_file('Homework text/names.txt')


######################## 3 ########################
def list_of_dates_dict_from_file(path_and_filename):
    with open(path_and_filename, 'r') as my_file:
        all_information_from_file = my_file.read()
    dates = []
    for data_line in all_information_from_file.split('\n'):
        only_some_date = data_line.split()[0:3]
        only_some_date = ' '.join(only_some_date)
        for split_some_date in only_some_date.split('-'):
            only_some_date = split_some_date.split()[0:3]
            if len(only_some_date) > 2:
                only_some_date = ' '.join(only_some_date)
                dates.append({'date': f'{only_some_date}'})
    with open(path_and_filename, 'w') as new_txt_file:
        new_txt_file.write(all_information_from_file)
    return dates


dates_from_file = list_of_dates_dict_from_file('Homework text/authors.txt')

######################## 4 ########################
