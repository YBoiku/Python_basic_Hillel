######################## 1 ########################
def list_of_domains_name_from_file(path_and_filename):
    with open(path_and_filename, 'r') as my_file:
        all_domains = my_file.read()
    domains_names = []
    for data_line in all_domains.split('\n'):
        if data_line[0] == '.':
            domains_names.append(data_line.split('.')[1])
    with open(path_and_filename, 'w') as new_txt_file:
        new_txt_file.write(all_domains)
    return domains_names


list_of_domains_names = list_of_domains_name_from_file('Homework text/domains.txt')
######################## 2 ########################
