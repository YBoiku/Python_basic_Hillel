import os
from typing import Optional


class DirectoryName:
    def __init__(self, directory_name: str):
        self.directory_name = directory_name
        self.first_method = self.dict_of_files_and_subfolders_in_folder()

    def dict_of_files_and_subfolders_in_folder(self) -> dict:
        list_dir = os.listdir(self.directory_name)
        files_list_in_dir = []
        folders_list_in_dir = []
        dict_of_files_and_subfolders = {'filenames': files_list_in_dir, 'dirnames': folders_list_in_dir}
        for filename_in_directory in list_dir:
            file_path_in_directory = os.path.join(self.directory_name, filename_in_directory)
            if os.path.isfile(file_path_in_directory):
                files_list_in_dir.append(''.join(file_path_in_directory.split(f'{self}\\')))
            elif os.path.isdir(file_path_in_directory):
                folders_list_in_dir.append(''.join(file_path_in_directory.split(f'{self}\\')))
        return dict_of_files_and_subfolders

    def sort_dict_list_to_alphabet_or_revers(self, sort_bool: Optional[bool] = None) -> dict:
        if sort_bool is True:
            ascii_sort_files = sorted(self.first_method['filenames'])
            ascii_sort_folders = sorted(self.first_method['dirnames'])
            self.first_method['filenames'] = ascii_sort_files
            self.first_method['dirnames'] = ascii_sort_folders
        elif sort_bool is False:
            rev_ascii_sort_files = sorted(self.first_method['filenames'])[::-1]
            rev_ascii_sort_folders = sorted(self.first_method['dirnames'])[::-1]
            self.first_method['filenames'] = rev_ascii_sort_files
            self.first_method['dirnames'] = rev_ascii_sort_folders
        return self.first_method

    def add_file_or_folder_in_existing_dict_lists(self, file_or_folder: str) -> dict:
        if file_or_folder.find('.') != -1:
            self.first_method.setdefault('filenames', []).append(file_or_folder)
        elif file_or_folder:
            self.first_method.setdefault('dirnames', []).append(file_or_folder)
        return self.first_method


path = DirectoryName('Homework_directory')
result_dict_list = path.dict_of_files_and_subfolders_in_folder()
result_sort = path.sort_dict_list_to_alphabet_or_revers(False)
add_file_or_folder = path.add_file_or_folder_in_existing_dict_lists('Anacondaz.txt')
print(add_file_or_folder)
