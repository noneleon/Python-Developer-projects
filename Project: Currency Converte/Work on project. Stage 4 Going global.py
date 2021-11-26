'''
Description
You can convert your conicoins into dollars, cool. What if you want a different currency? What if you're going to Morocco tomorrow? You'll need some dirhams, that's for sure. We need to improve our converter.

Take the imaginary exchange rates below and modify your program to work with 5 different currencies:

RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.
Take the number of conicoins as the user input, сonvert it to the specified currencies, and round the result to two decimals using the Python built-in function. Notice that the input number can have a fractional part!

Objectives
Get the number of conicoins from user input.
Print how much you will get in all five currencies mentioned above.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> 17
I will get 50.66 RUB from the sale of 17.0 conicoins.
I will get 13.94 ARS from the sale of 17.0 conicoins.
I will get 2.89 HNL from the sale of 17.0 conicoins.
I will get 33.36 AUD from the sale of 17.0 conicoins.
I will get 3.54 MAD from the sale of 17.0 conicoins.
Example 2:

> 3.5
I will get 10.43 RUB from the sale of 3.5 conicoins.
I will get 2.87 ARS from the sale of 3.5 conicoins.
I will get 0.6 HNL from the sale of 3.5 conicoins.
I will get 6.87 AUD from the sale of 3.5 conicoins.
I will get 0.73 MAD from the sale of 3.5 conicoins.
'''

# write your code here!
a = float(input())
print(f'I will get {round(a*2.98,2)} RUB from the sale of {a} conicoins.')
print(f'I will get {round(a*0.82,2)} ARS from the sale of {a} conicoins.')
print(f'I will get {round(a*0.17,2)} HNL from the sale of {a} conicoins.')
print(f'I will get {round(a*1.9622,2)} AUD from the sale of {a} conicoins.')
print(f'I will get {round(a*0.208,1)} MAD from the sale of {a} conicoins.')


\\

amount = float(input())
currencies = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
for k, v in currencies.items():
    print(f"I will get {round(amount * v, 2)} {k} from the sale of {amount} conicoins.")

    
\\

exchange_rates = {
    'RUB': 2.98,
    'ARS': 0.82,
    'HNL': 0.17,
    'AUD': 1.9622,
    'MAD': 0.208,
}

coin_count = float(input())
for k,v in exchange_rates.items():
    print(f"I will get {round(coin_count * v, 2)} {k} from the sale of {coin_count} conicoins.")


    
