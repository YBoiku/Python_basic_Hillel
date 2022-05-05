import os
from typing import Optional


class DirectoryName:
    def __init__(self, directory_name: str):
        self.directory_name = directory_name
        self.dict_of_files_and_subfolders_in_folder()

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
        dict_of_files_and_subfolders = self.dict_of_files_and_subfolders_in_folder()
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

    def add_file_or_folder_in_existing_dict_lists(self, file_or_folder: str) -> dict:
        dict_list_with_new_file_or_dir = self.dict_of_files_and_subfolders_in_folder()
        if file_or_folder.find('.') != -1:
            dict_list_with_new_file_or_dir.setdefault('filenames', []).append(file_or_folder)
        elif file_or_folder:
            dict_list_with_new_file_or_dir.setdefault('dirnames', []).append(file_or_folder)
        return dict_list_with_new_file_or_dir


path = DirectoryName('Homework_directory')
result_dict_list = path.dict_of_files_and_subfolders_in_folder()
result_sort = path.sort_dict_list_to_alphabet_or_revers(True)
add_file_or_folder = path.add_file_or_folder_in_existing_dict_lists('Anacondaz.txt')

