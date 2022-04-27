################ 1 ################
# def return_list_of_files_and_subfolders_in_folder(directory_name):
#     list_dir = os.listdir(directory_name)
#     x = []
#     y = []
#     for filename_in_directory in list_dir:
#         file_path_in_directory = os.path.join(path, filename_in_directory)
#         if os.path.isfile(file_path_in_directory):
#             x.append(file_path_in_directory)
#     for filename_in_directory in list_dir:
#         file_path_in_directory = os.path.join(path, filename_in_directory)
#         if os.path.isdir(file_path_in_directory):
#             y.append(file_path_in_directory)
#     z = {'filenames': x, 'dirnames': y}
#     return z
#
#
# path = 'Homework_directory'
# print(return_list_of_files_and_subfolders_in_folder(path))


# def return_list_of_files_and_subfolders_in_folder(directory_name):
#     list_dir = os.listdir(directory_name)
#     x = []
#     y = []
#     z = []
#     for filename_in_directory in list_dir:
#         file_path_in_directory = os.path.join(path, filename_in_directory)
#         if os.path.isfile(file_path_in_directory):
#             x.append(file_path_in_directory)
#         else:
#             y.append(file_path_in_directory)
#     z.append({'filenames': x, 'dirnames': y})
#     return z
#
#
# path = 'Homework_directory'
# print(return_list_of_files_and_subfolders_in_folder(path))


# def return_list_of_files_and_subfolders_in_folder(directory_name):
#     list_dir = os.listdir(directory_name)
#     x = []
#     y = []
#     z = []
#     for filename_in_directory in list_dir:
#         file_path_in_directory = os.path.join(path, filename_in_directory)
#         if os.path.isfile(file_path_in_directory):
#             x.append(''.join(file_path_in_directory.split(f'{path}\\')))
#         else:
#             y.append(''.join(file_path_in_directory.split(f'{path}\\')))
#     z.append({'filenames': x, 'dirnames': y})
#     return z
#
#
# path = 'Homework_directory'
# print(return_list_of_files_and_subfolders_in_folder(path))
################ 2 ################
