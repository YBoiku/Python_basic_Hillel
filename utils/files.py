def read_txt_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    return data