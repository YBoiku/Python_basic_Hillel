import json


def read_config(file_path: str) -> dict:
    with open(file_path, 'r') as my_file:
        dict_with_info = json.load(my_file)
    return dict_with_info


def rate():
    return f"1 USD/ {config_file['dollar course']} UAH"


def available():
    return f"UA account balance: {config_file['UA balance']}\nUSD account balance: {config_file['USD balance']}"


def buy(number: int):
    actual_uah = int(config_file['UA balance']) - number
    actual_usd = number / int(config_file['dollar course'])
    config_file['UA balance'] = round(actual_uah, 2)
    config_file['USD balance'] = round(actual_usd, 2)
    return config_file


def write_session_history():
    pass


config_file = read_config('config.json')
play = rate()
print(buy(2000))
