'''
Description
At this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!

There is a different amount of currencies in different tests. Checking if the input is empty might be useful.
Parse the data from FloatRates. You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache.

The very first currency is the one you want to exchange.
Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you.

Objectives
You're in the bank. Think about how much and what kind of currency you have.

Take the currency code, the currency code that the user wants to receive, and the amount of money the user has as the user input.
Retrieve the data from FloatRates as in the previous exercises.
Save the exchange rates for USD and EUR.
Read the currency to exchange for and the amount of money.
Take a look at the cache. Maybe you already have what you need?
If you have the currency in your cache, calculate the amount.
If not, get it from the site, and calculate the amount.
Save all the information to your cache.
Print the results.
Repeat steps 4-9 until there is no currency left to process.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> ILS
> USD
> 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.
Example 2:

> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.'''
import json
import requests


class Change:

    def __init__(self):
        self.money_user = None
        self.money_change = None
        self.have_money = None
        self.write_file = {}


    def money_currency(self):
        self.money_user = input().lower()
        self.money_change = input().lower()
        self.have_money = float(input())
        if self.money_user == 'usd' or self.money_change == 'usd':
                    print("Checking the cache...")
                    self.euro = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new_euro = self.euro.text
                    self.new_euro = json.loads(self.new_euro)
                    self.changed_euro = self.new_euro['eur']['rate']
                    self.write_file['eur'] = self.changed_euro

                    self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new = self.r.text
                    self.new = json.loads(self.new)
                    self.changed = self.new[self.money_change]['rate']
                    self.changed_money = self.have_money * self.changed
                    self.write_file[self.money_change] = self.changed
                    print(f"Oh! It is in the cache!\nYou received {round(self.changed_money, 2)} {self.money_change.upper()}.")

        elif self.money_user != 'usd' and self.money_user != 'eur':
                        print("Checking the cache...")
                        self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                        self.new = self.r.text
                        self.new = json.loads(self.new)
                        self.changed = self.new[self.money_change]['rate']
                        self.changed_money = (self.have_money * self.changed)
                        self.write_file[self.money_change] = self.changed
                        print(f"Sorry, but it is not in the cache!\nYou received {round(self.changed_money, 2)} {self.money_change.upper()}.")


        elif self.money_user == 'eur' or self.money_change == 'eur':
                    print("Checking the cache...")
                    self.usd = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new_usd = self.usd.text
                    self.new_usd = json.loads(self.new_usd)
                    self.changed_usd = self.new_usd['usd']['rate']
                    self.write_file['usd'] = self.changed_usd

                    self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new = self.r.text
                    self.new = json.loads(self.new)
                    self.changed = self.new[self.money_change]['rate']
                    self.changed_money = self.have_money * self.changed
                    self.write_file[self.money_change] = self.changed
                    print(f"Oh! It is in the cache!\nYou received {round(self.changed_money, 2)} {self.money_change.upper()}.")

        self.next_currency()

    def next_currency(self):
        self.money_usered = input().lower()
        while True:
            if len(self.money_usered) == 0:
                exit()
            if self.money_usered not in self.write_file.keys():
                        self.have_money = float(input())
                        print("Checking the cache...")
                        self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                        self.new = self.r.text
                        self.new = json.loads(self.new)
                        self.changed = self.new[self.money_usered]['rate']
                        self.changed_money = (self.have_money * self.changed)
                        self.write_file[self.money_usered] = self.changed
                        print(f"Sorry, but it is not in the cache!\nYou received {round(self.changed_money, 2)} {self.money_usered.upper()}.")
                        self.next_currency()
            elif self.money_usered in self.write_file.keys():
                        self.have_money = float(input())
                        print("Checking the cache...")
                        self.money_dict = self.write_file.get(self.money_usered)
                        self.changed_money = self.have_money * self.money_dict
                        print(f"Oh! It is in the cache!\nYou received {round(self.changed_money, 2)} {self.money_usered.upper()}.")
                        self.next_currency()






p = Change()
p.money_currency()

\\

import sys

import requests
import json


class Exchanger:
    user_currency = ""
    desired_currency = ""
    cash = 0
    base_currencies = ["USD", "EUR"]
    rates = {}
    json_data = {}
    connection = None

    def get_user_input(self):
        self.desired_currency = ""
        self.desired_currency = input()
        self.cash = float(input())

    def connect(self):
        url = f"http://www.floatrates.com/daily/{self.user_currency.lower()}.json"
        self.connection = requests.get(url)

    def get_rates(self):
        self.json_data = self.connection.json()
        self.rates = {rate.upper(): self.json_data[rate]["rate"] for rate in self.json_data if
                      rate.upper() in self.base_currencies}

    def add_rate(self):
        code = self.desired_currency
        rate = self.json_data[code.lower()]["rate"]
        self.rates.update({code.upper(): rate})

    def print_rate(self):
        code = self.desired_currency.upper()
        print(f"{self.cash} {self.user_currency.upper()} ==> {format(self.cash * self.rates[code], '.2f')} {code}.")

    def is_in_cache(self):
        print("Checking the cache...")
        return self.desired_currency.upper() in self.base_currencies

    def __init__(self):
        self.user_currency = input()
        while 1:
            self.desired_currency = input()
            if self.desired_currency == "":
                break
            try:
                self.cash = float(input())
                self.connect()
                self.get_rates()
                if self.is_in_cache():
                    print("Oh! It is in the cache!")
                else:
                    print("Sorry, but it is not in the cache!")
                    self.add_rate()
                    self.base_currencies.append(self.desired_currency.upper())
                self.print_rate()
            except:
                break


Exchanger()


\\

# write your code here!
import requests


class CurrencyConverter:

    def __init__(self, currency_in):
        self.currency_in = currency_in.lower()
        self.rates = {self.currency_in: 1.0}
        self.retrieve_rate("EUR", False)
        self.retrieve_rate("USD", False)

    def retrieve_rate(self, curr, log=True):
        curr = curr.lower()
        if log:
            print("Checking the cache...")
        if not self.rates.get(curr, False):
            if log:
                print("Sorry, but it is not in the cache!")
            self.rates[curr] = requests.get(f"http://www.floatrates.com/daily/{self.currency_in}.json").json()[curr]["rate"]
        else:
            if log:
                print("Oh! It is in the cache!")
        return self.rates[curr]

    def convert_to_currency(self, curr, amount):
        return round(self.retrieve_rate(curr) * amount, 2)


def main():
    currency_in = input()
    convertor = CurrencyConverter(currency_in)

    while True:
        currency_out = input()
        if not currency_out:
            return
        money = float(input())
        print(f"You received {convertor.convert_to_currency(currency_out, money)} {currency_out}.")


if __name__ == "__main__":
    main()

