'''
Description
In the previous stages, we worked with different real-world currencies but the exchange rates were fixed. Unfortunately (or not, depending on your political stance), we don't really have fixed exchange rates in today's world. At this stage, you will have to work with the Internet to get the information! The FloatRates site contains a special JSON page for each currency. Your task is to make requests to these pages and download the actual data on the exchange rates of the US dollar and the euro. Remember, that the data is stored in JSON format.

Objectives
There are many currency codes, for example, RUB, ARS, HNL, AUD, MAD, etc. Choose the one you like best and return the information about the exchange rates from the site specified above for only two currencies: USD and EUR.

Select one currency code, take it as the user input.
Make a request to http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json. Don't forget that you need to put the code in lowercase.
Print your result for USD and EUR.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

The results of your output may differ, as the service updates the data once in twelve hours. Don't hesitate to print the whole string for your own interest, but it is not a part of the stage.
The output for HNL:

> HNL
{'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 0.040212252288502, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 24.868042526579}
{'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 0.035775653590882, 
'''

import requests
import json


def exchange_to_dollar():
    no_of_conicoins = int(input("Please, enter the number of conicoins you have: "))
    exchange_rate = float(input("Please, enter the exchange rate: "))
    dollars = round((exchange_rate * no_of_conicoins), 2)
    print(f"The total amount of dollars: {dollars}")


def exchange_conicoins():
    exchange_rate = {
        "RUB": 2.98,
        "ARS": 0.82,
        "HNL": 0.17,
        "AUD": 1.9622,
        "MAD": 0.208,
    }

    no_of_conicoins = float(input())

    for currency in exchange_rate.keys():
        money_from_conicoins = round((exchange_rate[currency] * no_of_conicoins), 2)
        print(f"I will get {money_from_conicoins} {currency} "
              f"from the sale of {no_of_conicoins} conicoins.")


def real_world_exchange():
    user_input = input().lower()
    coin = requests.get(f"http://www.floatrates.com/daily/{user_input}.json")
    data = json.loads(s=coin.content)
    print(data['usd'])
    print(data['eur'])


real_world_exchange()


\\

import requests
import json
current_coin = input()
r = requests.get(f"http://www.floatrates.com/daily/{current_coin}.json").content
dict_from_json = json.loads(r)
print(dict_from_json['usd'])
print(dict_from_json['eur'])


\\


# write your code here!
import requests
import json

current_coin = input()

request_coin_url = f"http://www.floatrates.com/daily/{current_coin}.json"
r = requests.get(request_coin_url)
response_content = r.content
dict_from_json = json.loads(response_content)
print(dict_from_json['usd'])
print(dict_from_json['eur'])

