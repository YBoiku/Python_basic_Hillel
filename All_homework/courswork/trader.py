import json
import random
from typing import Optional
from argparse import ArgumentParser


class Trader:
    def __init__(self, info_path, history_info_path):
        self.info_path = info_path
        self.history_info_path = history_info_path
        self.account_info = self.read_config()
        self.ua_balance = self.account_info['UA balance']
        self.usd_balance = self.account_info['USD balance']
        self.usd_course = self.account_info['dollar course']

    def read_config(self) -> dict:
        try:
            with open(self.history_info_path, 'r') as file:
                dict_with_info = json.load(file)
        except:
            with open(self.info_path, 'r') as file:
                dict_with_info = json.load(file)
        return dict_with_info

    def rate(self):
        print(f"1 USD / {self.usd_course} UAH")

    def available(self):
        print(f"UA account balance: {self.ua_balance}"
              f"\nUSD account balance: {self.usd_balance}")

    def buy(self, number: Optional[int] = 0) -> dict:
        need_uah = number * self.usd_course
        if need_uah > self.ua_balance:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.ua_balance}, AVAILABLE {need_uah}")
        else:
            actual_uah = self.ua_balance - need_uah
            actual_usd = number
            self.account_info['UA balance'] = round(actual_uah, 2)
            self.account_info['USD balance'] += round(actual_usd, 2)
            print(self.account_info)
        return self.account_info

    def sell(self, available: Optional[int] = 0) -> dict:
        if available > self.usd_balance:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {self.usd_balance}, AVAILABLE {available}")
        else:
            actual_usd: int = self.usd_balance - available
            actual_uah: int = available * self.usd_course
            self.account_info['USD balance'] = round(actual_usd, 2)
            self.account_info['UA balance'] += round(actual_uah, 2)
            print(self.account_info)
        return self.account_info

    def buy_all(self):
        actual_uah: int = 0
        actual_usd: int = self.account_info['UA balance'] / self.account_info['dollar course']
        # self.account_info['UA balance'] = self.account_info['UA balance'] - self.account_info['UA balance']
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
        actual_course: int = self.usd_course
        delta: int = self.account_info["delta"]
        max_range_course: int = actual_course + delta
        min_range_course: int = actual_course - delta
        new_course = random.uniform(max_range_course, min_range_course)
        self.account_info['dollar course'] = round(new_course, 2)
        return self.account_info

    # def restart(self):
    #     pass


def write_session_history(data):
    with open("trader_session_history.json", 'w') as file:
        json.dump(data, file, indent=2)


args = ArgumentParser()
args.add_argument("CLI")
args.add_argument("SUM", type=int, nargs='?', default=0)
# args.add_argument("ALL")
args = vars(args.parse_args())
print(args)
amount = args["SUM"]
config_file = Trader("config.json", "trader_session_history.json")
if args["CLI"] == "RATE":
    config_file.rate()
elif args["CLI"] == "AVAILABLE":
    config_file.available()
elif args["CLI"] == "BUY":
    write_session_history(config_file.buy(amount))
elif args["CLI"] == "SELL":
    write_session_history(config_file.sell(amount))
elif args["CLI"] == "BUY" and args["SUM"] == "ALL":
    write_session_history(config_file.buy_all())
elif args["CLI"] == "SELL" and args["SUM"] == "ALL":
    write_session_history(config_file.sell_all())
elif args["CLI"] == "NEXT":
    write_session_history(config_file.next())
# elif args["CLI"] == "RESTART":
#     config_file.restart()
