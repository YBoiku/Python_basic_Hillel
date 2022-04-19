DEBUG_MOD = True


def read_txt_file_as_str(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    return data


if __name__ == 'main':
    print('>>>>>>>>>>>>>>>>>>>>', __name__)
    data = read_txt_file_as_str('test_1.txt')
    print('>>>>>>>>>>>>>>>>>>>>', data)
