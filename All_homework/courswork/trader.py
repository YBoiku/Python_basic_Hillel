import json
import random
from typing import Optional
from argparse import ArgumentParser
import os


class Trader:
    def __init__(self, info_path, history_info_path):
        self.info_path = info_path
        self.history_info_path = history_info_path
        self.account_info = self.read_config()
        self.ua_balance = self.account_info['UA balance']
        self.usd_balance = self.account_info['USD balance']
        self.usd_course = self.account_info['dollar course']

    def read_config(self) -> dict:
        if os.path.isfile(self.history_info_path) is False:
            with open(self.info_path, 'r') as file:
                dict_with_info = json.load(file)
        else:
            with open(self.history_info_path, 'r') as file:
                dict_with_info = json.load(file)
        return dict_with_info

    def rate(self):
        print(f"1 USD / {self.usd_course} UAH")
        return self.account_info

    def available(self):
        print(f"UA account balance: {self.ua_balance}"
              f"\nUSD account balance: {self.usd_balance}")
        return self.account_info

    def buy(self, available: Optional[int] = 0) -> dict:
        need_uah = available * self.usd_course
        if need_uah > self.ua_balance:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.ua_balance}, AVAILABLE {need_uah}")
        else:
            actual_uah = self.ua_balance - need_uah
            actual_usd = available
            self.account_info['UA balance'] = round(actual_uah, 2)
            self.account_info['USD balance'] += round(actual_usd, 2)
        return self.account_info

    def sell(self, available: int) -> dict:
        if available > self.usd_balance:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {self.usd_balance}, AVAILABLE {available}")
        else:
            actual_usd: int = self.usd_balance - available
            actual_uah: int = available * self.usd_course
            self.account_info['UA balance'] += round(actual_uah, 2)
            self.account_info['USD balance'] = round(actual_usd, 2)
        return self.account_info

    def buy_all(self) -> dict:
        if self.ua_balance == 0:
            print(f"YOUR CURRENT BALANCE UAH {self.ua_balance}")
        else:
            actual_uah: int = 0
            actual_usd: int = self.ua_balance / self.usd_course
            self.account_info['UA balance'] = round(actual_uah, 2)
            self.account_info['USD balance'] += round(actual_usd, 2)
        return self.account_info

    def sell_all(self) -> dict:
        if self.usd_balance == 0:
            print(f"YOUR CURRENT BALANCE USD {self.usd_balance}")
        else:
            actual_uah = self.usd_balance * self.usd_course
            actual_usd = 0
            self.account_info['UA balance'] += round(actual_uah, 2)
            self.account_info['USD balance'] = round(actual_usd, 2)
        return self.account_info

    def next(self) -> dict:
        actual_course: int = self.usd_course
        delta: int = self.account_info["delta"]
        max_range_course: int = actual_course + delta
        min_range_course: int = actual_course - delta
        new_course = random.uniform(max_range_course, min_range_course)
        self.account_info['dollar course'] = round(new_course, 2)
        return self.account_info

    def restart(self):
        os.remove(self.history_info_path)


def write_session_history(data):
    with open("trader_last_session.json", 'w') as file:
        json.dump(data, file, indent=2)


args = ArgumentParser()
args.add_argument("CLI")
args.add_argument("SUM", type=str, nargs='?', default=0)
args = vars(args.parse_args())
amount = args["SUM"]
config_file = Trader("config.json", "trader_last_session.json")
if args["CLI"] == "RATE":
    config_file.rate()
elif args["CLI"] == "AVAILABLE":
    config_file.available()
elif args["CLI"] == "BUY" and args["SUM"] != "ALL":
    write_session_history(config_file.buy(int(amount)))
elif args["CLI"] == "SELL" and args["SUM"] != "ALL":
    write_session_history(config_file.sell(int(amount)))
elif args["CLI"] == "BUY" and args["SUM"] == "ALL":
    write_session_history(config_file.buy_all())
elif args["CLI"] == "SELL" and args["SUM"] == "ALL":
    write_session_history(config_file.sell_all())
elif args["CLI"] == "NEXT":
    write_session_history(config_file.next())
elif args["CLI"] == "RESTART":
    config_file.restart()
