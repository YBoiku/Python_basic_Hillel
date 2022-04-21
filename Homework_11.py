import os


################ 1 ################
def dict_lists_of_files_and_subfolders_in_folder(directory_name):
    list_dir = os.listdir(directory_name)
    files_list_in_dir = []
    folders_list_in_dir = []
    dict_lists_of_files_and_subfolders = []
    for filename_in_directory in list_dir:
        file_path_in_directory = os.path.join(path, filename_in_directory)
        if os.path.isfile(file_path_in_directory):
            files_list_in_dir.append(''.join(file_path_in_directory.split(f'{path}\\')))
        else:
            folders_list_in_dir.append(''.join(file_path_in_directory.split(f'{path}\\')))
    dict_lists_of_files_and_subfolders.append({'filenames': files_list_in_dir, 'dirnames': folders_list_in_dir})
    return dict_lists_of_files_and_subfolders


path = 'Homework_directory'
result = dict_lists_of_files_and_subfolders_in_folder(path)
