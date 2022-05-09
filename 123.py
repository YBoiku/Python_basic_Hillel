import json
import random
import typing



def read_config(file_path: str) -> dict:
    with open(file_path, 'r') as my_file:
        dict_with_info = json.load(my_file)
    return dict_with_info


def rate():
    return f"1 USD/ {config_file['dollar course']} UAH"


def available():
    return f"UA account balance: {config_file['UA balance']}\nUSD account balance: {config_file['USD balance']}"


def buy(number: int):
    need_uah = number * config_file['dollar course']
    if need_uah > config_file['UA balance']:
        return f"UNAVAILABLE, REQUIRED BALANCE UAH {config_file['UA balance']}, AVAILABLE {need_uah}"
    else:
        actual_uah = config_file['UA balance'] - number
        actual_usd = number / config_file['dollar course']
        config_file['UA balance'] = round(actual_uah, 2)
        config_file['USD balance'] += round(actual_usd, 2)
        return config_file


def sell(number: int):
    if number > config_file['USD balance']:
        return f"UNAVAILABLE, REQUIRED BALANCE USD {config_file['USD balance']}, AVAILABLE {number}"
    else:
        actual_usd: int = config_file['USD balance'] - number
        actual_uah: int = number * config_file['dollar course']
        config_file['USD balance'] = round(actual_usd, 2)
        config_file['UA balance'] += round(actual_uah, 2)
        return config_file


def buy_all() -> dict:
    actual_uah: int = 0
    actual_usd: int = config_file['UA balance'] / config_file['dollar course']
    config_file['UA balance'] = actual_uah
    config_file['USD balance'] += round(actual_usd, 2)
    return config_file


def sell_all() -> dict:
    actual_uah = config_file['USD balance'] * config_file['dollar course']
    actual_usd = 0
    config_file['UA balance'] += round(actual_uah, 2)
    config_file['USD balance'] = actual_usd
    return config_file


def next() -> dict:
    actual_course: int = config_file['dollar course']
    delta: int = config_file["delta"]
    max_range_course: int = actual_course + delta
    min_range_course: int = actual_course - delta
    new_course = random.uniform(max_range_course, min_range_course)
    config_file['dollar course'] = round(new_course, 2)
    return config_file



def restart():
    pass


def write_session_history():
    pass


config_file = read_config('config.json')
play = rate()
print(next())
