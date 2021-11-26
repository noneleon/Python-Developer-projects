'''
Description
Finally, let's add to our calculator the capacity to compute differentiated payments. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. Let’s look at the formula:

D_m = \dfrac{P}{n} + i * \left( P - \dfrac{P*(m-1)}{n} \right)D 
m
​
 = 
n
P
​
 +i∗(P− 
n
P∗(m−1)
​
 )

Where:

D_mD 
m
​
  = mth differentiated payment;

PP = the loan principal;

ii = nominal interest rate. This is usually 1/12 of the annual interest rate, and it’s usually a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.

nn = number of payments. This is usually the number of months in which repayments will be made.

mm = current repayment month.

The user has to input a lot of parameters, so it might be convenient to use command-line arguments.

You can run your loan calculator via command line like this:

python creditcalc.py
Using command-line arguments you can run your program this way:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
This way, your program can get different values without prompting the user to input them. It can be useful when you are developing your program and trying to find a mistake, and you want to run the program with the same parameters again and again. It's also convenient if you made a mistake in a single parameter: you don't have to input all the other values again.

Objectives
In this stage, you are going to implement the following features:

Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).
The final version of your program is supposed to work from the command line and parse the following parameters:

--type indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
--payment is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too:
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
--periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing:
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
You should also display an error message when negative values are entered:

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

Example 1: calculating differentiated payments

> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
In this example, the user wants to take a loan with differentiated payments. You know the principal, the count of periods, and interest, which are 1,000,000, 10 months, and 10%, respectively.

The calculator should calculate payments for all 10 months. Let’s look at the formula above. In this case:

P = 1000000P=1000000
n = 10n=10
i = \dfrac{ interest }{ 12 * 100\% } = \dfrac { 10\% }{12 * 100\% } = 0.008333...i= 
12∗100%
interest
​
 = 
12∗100%
10%
​
 =0.008333...

Now let’s calculate the payment for the first month:

D_1 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(1-1) }{ 10 } \right) = 108333.333...D 
1
​
 = 
n
P
​
 +i∗(P− 
n
P∗(m−1)
​
 )= 
10
1000000
​
 +0.008333...∗(1000000− 
10
1000000∗(1−1)
​
 )=108333.333...

The second month (m = 2m=2):

D_2 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(2-1) }{ 10 } \right) = 107500D 
2
​
 = 
n
P
​
 +i∗(P− 
n
P∗(m−1)
​
 )= 
10
1000000
​
 +0.008333...∗(1000000− 
10
1000000∗(2−1)
​
 )=107500

The third month (m = 3m=3):

D_3 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(3-1) }{ 10 } \right) = 106666.666...D 
3
​
 = 
n
P
​
 +i∗(P− 
n
P∗(m−1)
​
 )= 
10
1000000
​
 +0.008333...∗(1000000− 
10
1000000∗(3−1)
​
 )=106666.666...

And so on. You can see other monthly payments above.

Your loan calculator should output monthly payments for every month as in the first stage. Also, round up all floating-point values.
Finally, your loan calculator should add up all the payments and subtract the loan principal so that you get the overpayment.

Example 2: calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest

> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
Example 3: fewer than four arguments are given

> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
Example 4: calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%

> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628
Example 5: calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest

> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622
Example 6: calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest

> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000

'''
import argparse
import math

pay_type = None
payment = None
principal = None
periods = None
interest = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', help='the type of payments: "annuity" or "diff" (differentiated)')
    parser.add_argument('--payment', help='monthly payment', type=int)
    parser.add_argument('--principal', help='to calculate payment', type=int)
    parser.add_argument('--periods', help='the number of months and/or years needed to repay the credit', type=int)
    parser.add_argument('--interest', help='is specified without a percent sign', type=float)

    if parse_args(parser.parse_args()):
        if pay_type == 'annuity':
            if payment is None:
                calculate_payment()
            elif principal is None:
                calculate_principal()
            elif periods is None:
                calculate_periods()
        elif pay_type == "diff":
            calculate_differentiated()
    else:
        print('Incorrect parameters')


def parse_args(args):
    global pay_type
    global payment
    global principal
    global periods
    global interest

    if args.principal and args.principal >= 0:
        principal = args.principal

    if args.periods and args.periods >= 0:
        periods = args.periods

    if args.interest and args.interest >= 0.0:
        interest = args.interest
        if args.type:
            pay_type = args.type

            if args.type == "annuity":
                if args.payment and args.payment >= 0:
                    payment = args.payment
                if (principal is None and periods is None) or \
                        (periods is None and payment is None) or \
                        (payment is None and principal is None):
                    return False
                return True
            elif args.type == "diff":
                if args.payment:
                    return False
                elif principal is not None and periods is not None:
                    return True

    return False


def calculate_payment():
    i = interest / 100 / 12
    annuity = principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    over = math.ceil(annuity) * periods - principal
    print(f'Your annuity payment = {math.ceil(annuity)}!')
    print(f'Overpayment = {over}')


def calculate_principal():
    i = interest / 100 / 12
    P = payment / ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    over = payment * periods - math.floor(P)
    print(f'Your credit principal = {math.floor(P)}!')
    print(f'Overpayment = {over}')


def calculate_periods():
    i = interest / 100 / 12
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    q, r = divmod(n, 12)
    year_str = 'year'
    if q > 1:
        year_str += 's'
    month_str = 'month'
    if r > 1:
        month_str += 's'
    over = payment * n - principal
    if r > 0:
        print(f'You need {q} {year_str} and {r} {month_str} to repay this credit!')
    else:
        print(f'You need {q} {year_str} to repay this credit!')
    print(f'Overpayment = {over}')


def calculate_differentiated():
    i = interest / 100 / 12
    total = 0
    for m in range(1, periods + 1):
        D = principal / periods + i * (principal - principal * (m - 1) / periods)
        total += math.ceil(D)
        print(f'Month {m}: paid out {math.ceil(D)}')
    print()
    over = total - principal
    print(f'Overpayment = {over}')


if __name__ == '__main__':
    main()
\\

import argparse
import math

parser = argparse.ArgumentParser(description="Calculation of differentiated and annuity payments")
parser.add_argument("--type", choices=["diff", "annuity"], help="You need to choose type of payments")
parser.add_argument("--payment", type=int, help="Input the monthly payment amount")
parser.add_argument("--principal", type=int, help="Input the loan principal")
parser.add_argument("--periods", type=int, help="Input the number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="Input interest rate")

args = parser.parse_args()

# annuity payment
if args.type is not None and args.type not in "diff" and args.payment is not None \
        and args.principal is not None and args.interest is not None:
    # annuity payment's input: --payment, --principal, --interest
    if args.principal > 0 and args.payment > 0 and args.interest > 0:
        year_months = 12
        i = args.interest / (year_months * 100)  # the nominal interest rate
        x = args.payment / (args.payment - i * args.principal)
        n = math.log(x, 1 + i)  # the number of months
        years = math.ceil(n) // year_months
        months = math.ceil(n) - years * year_months
        overpayment = (args.payment * math.ceil(n)) - args.principal
        if years == 0 and months > 1:
            print(f'It will take {months} months to repay this loan!')
        elif years == 0 and months == 1:
            print(f'It will take {months} month to repay this loan!')
        else:
            if years > 1 and months == 0:
                print(f'It will take {years} years to repay this loan!')
            elif years == 1 and months == 0:
                print(f'It will take {years} year to repay this loan!')
            else:
                print(f'It will take {years} year and {months} months to repay this loan!')
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
elif args.type is not None and args.type not in "diff" and args.periods is not None \
        and args.principal is not None and args.interest is not None:
    # annuity payment's input: --principal, --periods, --interest
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        year_months = 12
        i = args.interest / (year_months * 100)  # the nominal interest rate
        annuity = args.principal * (i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)
        overpayment = math.ceil(annuity) * args.periods - args.principal
        print(f'Your annuity payment = {math.ceil(annuity)}!')
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
elif args.type is not None and args.type not in "diff" and args.periods is not None \
        and args.payment is not None and args.interest is not None:
    # annuity payment's input: --payment, --periods, --interest
    if args.payment > 0 and args.periods > 0 and args.interest > 0:
        year_months = 12
        i = float(args.interest) / (year_months * 100)  # the nominal interest rate
        loan_principal = args.payment / (i * math.pow(i + 1, args.periods) / (math.pow(i + 1, args.periods) - 1))
        overpayment = (args.payment * args.periods) - loan_principal
        print(f'Your loan principal = {math.floor(loan_principal)}!')
        print(f"Overpayment = {math.ceil(overpayment)}")
    else:
        print("Incorrect parameters")
# differentiated payment
elif args.type is not None and args.type not in "annuity" and args.principal is not None \
        and args.periods is not None and args.interest is not None:
    # differentiated payment's input: --principal, --periods, --interest
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        payment = 0
        for m in range(1, args.periods + 1, 1):
            year_months = 12
            i = args.interest / (year_months * 100)  # the nominal interest rate
            diff = args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods)
            payment += math.ceil(diff)
            print(f"Month {m}: payment is {math.ceil(diff)}")
        overpayment = payment - args.principal
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
\\

import math
import argparse
import sys


def pluralize(word, quantity):
    if quantity == 0:
        return ''
    plural = '' if quantity == 1 else 's'
    return f'{quantity} {word}{plural}'


class LoanCalculator:

    def __init__(self, loan_type, principal, payment, periods, interest):
        self.loan_type = loan_type
        self.principal = int(principal) if principal else 0
        self.payment = int(payment) if payment else 0
        self.periods = int(periods) if periods else 0
        self.interest = float(interest) / 1200
        self.overpayment = 0
        self.calculate()

    def set_default_overpayment(self):
        self.overpayment = int(self.payment * self.periods - self.principal)
        
    def calculate(self):
        if self.loan_type == 'diff':
            if self.payment == 0:
                [print(month) for month in self.get_differentiated_payments()]
                print()
        elif self.loan_type == 'annuity':
            if self.payment == 0:
                print(self.get_annuity_payment())
            elif self.principal == 0:
                print(self.get_annuity_principal())
            elif self.periods == 0:
                print(self.get_time_to_repay())
        print(self.get_overpayment())

    def get_annuity_principal(self):
        a = self.payment
        n = self.periods
        i = self.interest
        self.principal = p = int(a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
        self.set_default_overpayment()
        return f"Your loan principal = {self.principal}!"

    def get_annuity_payment(self):
        p = self.principal
        n = self.periods
        i = self.interest
        self.payment = math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
        self.set_default_overpayment()
        return f"Your annuity payment = {self.payment}!"

    def get_differentiated_payments(self):
        p = self.principal
        n = self.periods
        i = self.interest
        self.payment = [math.ceil((p / n) + i * (p - ((p * (m - 1)) / n))) for m in range(1, n + 1)]
        self.overpayment = int(sum(self.payment) - p)
        return [f"Month {m + 1}: payment is {self.payment[m]}" for m in range(0, len(self.payment))]

    def get_time_to_repay(self):
        p = self.principal
        a = self.payment
        i = self.interest
        self.periods = math.ceil(math.log(a / (a - i * p), 1 + i))
        self.set_default_overpayment()
        y = pluralize('year', math.floor(self.periods / 12))
        m = pluralize('month', self.periods % 12)
        conjunction = ' and ' if y and m else ''
        return f"It will take {y + conjunction + m} to repay this loan!"

    def get_overpayment(self):
        return f"Overpayment = {self.overpayment}"


error_message = "Incorrect parameters."
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

if args.type != 'annuity' and args.type != 'diff':
    print(error_message)
elif args.type is None or args.interest is None:
    print(error_message)
elif args.type == 'diff' and args.payment:
    print(error_message)
elif len(sys.argv) < 5:
    print(error_message)
elif (args.principal and int(args.principal) < 0)\
        or (args.payment and float(args.payment) < 0)\
        or (args.periods and int(args.periods) < 0)\
        or (args.interest and float(args.interest) < 0):
    print(error_message)
else:
    LoanCalculator(args.type, args.principal, args.payment, args.periods, args.interest)

