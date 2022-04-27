import os


################ 1 ################
def dict_of_files_and_subfolders_in_folder(directory_name: str) -> dir:
    list_dir = os.listdir(directory_name)
    files_list_in_dir = []
    folders_list_in_dir = []
    dict_of_files_and_subfolders = {'filenames': files_list_in_dir, 'dirnames': folders_list_in_dir}
    for filename_in_directory in list_dir:
        file_path_in_directory = os.path.join(path, filename_in_directory)
        if os.path.isfile(file_path_in_directory):
            files_list_in_dir.append(''.join(file_path_in_directory.split(f'{path}\\')))
        elif os.path.isdir(file_path_in_directory):
            folders_list_in_dir.append(''.join(file_path_in_directory.split(f'{path}\\')))
    return dict_of_files_and_subfolders


path = 'Homework_directory'
result_dict_list = dict_of_files_and_subfolders_in_folder(path)


################ 2 ################
def sort_dict_list_to_alphabet_or_revers(directory_name: str, sort_bool: bool) -> dir:
    dict_of_files_and_subfolders = dict_of_files_and_subfolders_in_folder(directory_name)
    if sort_bool is True:
        ascii_sort_files = sorted(dict_of_files_and_subfolders['filenames'])
        ascii_sort_folders = sorted(dict_of_files_and_subfolders['dirnames'])
        dict_of_files_and_subfolders['filenames'] = ascii_sort_files
        dict_of_files_and_subfolders['dirnames'] = ascii_sort_folders
    elif sort_bool is False:
        rev_ascii_sort_files = sorted(dict_of_files_and_subfolders['filenames'])[::-1]
        rev_ascii_sort_folders = sorted(dict_of_files_and_subfolders['dirnames'])[::-1]
        dict_of_files_and_subfolders['filenames'] = rev_ascii_sort_files
        dict_of_files_and_subfolders['dirnames'] = rev_ascii_sort_folders
    return dict_of_files_and_subfolders


result_sort = sort_dict_list_to_alphabet_or_revers(path, False)


################ 3 ################
def add_file_or_folder_in_existing_dict_lists(dict_with_file_and_folder: dict, file_or_folder: str) -> dict:
    if file_or_folder.find('.') != -1:
        dict_with_file_and_folder.setdefault('filenames', []).append(file_or_folder)
    elif file_or_folder:
        dict_with_file_and_folder.setdefault('dirnames', []).append(file_or_folder)
    return dict_with_file_and_folder


add_file_or_folder = add_file_or_folder_in_existing_dict_lists(result_dict_list, 'Anacondaz.txt')
