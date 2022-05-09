import json
import os
import random
from typing import Optional
import sys


class Trader:
    def __init__(self, path_info: str):
        self.path_info = os.path.join(os.path.dirname(sys.argv[0]), path_info)  # под вопросом
        self.account_info = self.read_config()

    def read_config(self) -> dict:
        with open(self.path_info, 'r') as file:
            dict_with_info = json.load(file)
        return dict_with_info

    def rate(self):
        return f"1 USD/ {self.account_info['dollar course']} UAH"

    def available(self):
        return f"UA account balance: {self.account_info['UA balance']}" \
               f"\nUSD account balance: {self.account_info['USD balance']}"

    def buy(self, number: Optional[int] = None):
        need_uah = number * self.account_info['dollar course']
        if need_uah > self.account_info['UA balance']:
            return f"UNAVAILABLE, REQUIRED BALANCE UAH {self.account_info['UA balance']}, AVAILABLE {need_uah}"
        else:
            actual_uah = self.account_info['UA balance'] - number
            actual_usd = number / self.account_info['dollar course']
            self.account_info['UA balance'] = round(actual_uah, 2)
            self.account_info['USD balance'] += round(actual_usd, 2)
            return self.account_info

    def sell(self, number: Optional[int] = None):
        if number > self.account_info['USD balance']:
            return f"UNAVAILABLE, REQUIRED BALANCE USD {self.account_info['USD balance']}, AVAILABLE {number}"
        else:
            actual_usd: int = self.account_info['USD balance'] - number
            actual_uah: int = number * self.account_info['dollar course']
            self.account_info['USD balance'] = round(actual_usd, 2)
            self.account_info['UA balance'] += round(actual_uah, 2)
            return self.account_info

    def buy_all(self) -> dict:
        actual_uah: int = 0
        actual_usd: int = self.account_info['UA balance'] / self.account_info['dollar course']
        self.account_info['UA balance'] = actual_uah
        self.account_info['USD balance'] += round(actual_usd, 2)
        return self.account_info

    def sell_all(self) -> dict:
        actual_uah = self.account_info['USD balance'] * self.account_info['dollar course']
        actual_usd = 0
        self.account_info['UA balance'] += round(actual_uah, 2)
        self.account_info['USD balance'] = actual_usd
        return self.account_info

    def next(self) -> dict:
        actual_course: int = self.account_info['dollar course']
        delta: int = self.account_info["delta"]
        max_range_course: int = actual_course + delta
        min_range_course: int = actual_course - delta
        new_course = random.uniform(max_range_course, min_range_course)
        self.account_info['dollar course'] = round(new_course, 2)
        return self.account_info

    def restart(self):
        pass

    def write_session_history(self):
        pass


config_file = Trader('config.json')
result = config_file.sell(10)
