import json
import random
from typing import Optional
from argparse import ArgumentParser


class Trader:
    def __init__(self, path_info, path_history_info):
        self.path_info = path_info
        self.session = 'trader_session_history.json'
        self.account_info = self.read_config()

    def read_config(self) -> dict:
        with open(self.path_info, 'r') as file:
            dict_with_info = json.load(file)
        return dict_with_info

    def rate(self):
        print(f"1 USD / {self.account_info['dollar course']} UAH")

    def available(self):
        print(f"UA account balance: {self.account_info['UA balance']}"
              f"\nUSD account balance: {self.account_info['USD balance']}")

    def buy(self, number: Optional[int] = None):
        need_uah = number * self.account_info['dollar course']
        if need_uah > self.account_info['UA balance']:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.account_info['UA balance']}, AVAILABLE {need_uah}")
        else:
            actual_uah = self.account_info['UA balance'] - number
            actual_usd = number / self.account_info['dollar course']
            self.account_info['UA balance'] = round(actual_uah, 2)
            self.account_info['USD balance'] += round(actual_usd, 2)
            print(self.account_info)

    def sell(self, number: Optional[int] = None):
        if number > self.account_info['USD balance']:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {self.account_info['USD balance']}, AVAILABLE {number}")
        else:
            actual_usd: int = self.account_info['USD balance'] - number
            actual_uah: int = number * self.account_info['dollar course']
            self.account_info['USD balance'] = round(actual_usd, 2)
            self.account_info['UA balance'] += round(actual_uah, 2)
            print(self.account_info)

    def buy_all(self):
        actual_uah: int = 0
        actual_usd: int = self.account_info['UA balance'] / self.account_info['dollar course']
        self.account_info['UA balance'] = actual_uah
        self.account_info['USD balance'] += round(actual_usd, 2)
        return self.account_info

    def sell_all(self):
        actual_uah = self.account_info['USD balance'] * self.account_info['dollar course']
        actual_usd = 0
        self.account_info['UA balance'] += round(actual_uah, 2)
        self.account_info['USD balance'] = actual_usd
        return self.account_info

    def next(self):
        actual_course: int = self.account_info['dollar course']
        delta: int = self.account_info["delta"]
        max_range_course: int = actual_course + delta
        min_range_course: int = actual_course - delta
        new_course = random.uniform(max_range_course, min_range_course)
        self.account_info['dollar course'] = round(new_course, 2)
        return self.account_info

    def restart(self):
        pass


def write_session_history(data):
    with open("trader_session_history.json", 'w') as file:
        json.dump(data, file)


args = ArgumentParser()
args.add_argument("CLI")
args = vars(args.parse_args())
config_file = Trader("config.json")
history_config_file = Trader("trader_session_history.json")
if args["CLI"] == "RATE":
    config_file.rate()
elif args["CLI"] == "AVAILABLE":
    config_file.available()
elif args["CLI"] == "BUY":
    config_file.buy()
elif args["CLI"] == "SELL":
    config_file.sell()
elif args["CLI"] == "BUY_ALL":
    write_session_history(config_file.buy_all())
elif args["CLI"] == "SELL_ALL":
    write_session_history(config_file.sell_all())
elif args["CLI"] == "NEXT":
    write_session_history(config_file.next())
elif args["CLI"] == "RESTART":
    config_file.restart()
