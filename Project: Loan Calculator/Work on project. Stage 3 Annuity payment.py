'''
Description
Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.

Here is the formula:

A_{ordinary\_annuity} = P * \dfrac{i * (1+i)^n}{(1+i)^n-1}A 
ordinary_annuity
​
 =P∗ 
(1+i) 
n
 −1
i∗(1+i) 
n
 
​
 

Where:

AA = annuity payment;

PP = loan principal;

ii = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;

nn = number of payments. This is usually the number of months in which repayments will be made.

You are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can be calculated if others are known:

Loan principal:

P = \dfrac{A}{\left( \dfrac{i * (1+i)^n}{(1+i)^n-1} \right)}P= 
( 
(1+i) 
n
 −1
i∗(1+i) 
n
 
​
 )
A
​
 

The number of payments:

n = \log_{1+i} \left( \dfrac{A}{A - i*P} \right)n=log 
1+i
​
 ( 
A−i∗P
A
​
 )

Objectives
In this stage, you should add new behavior to the calculator:

First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
Then, you need to ask them to input the remaining values.
Finally, compute and output the value that they wanted.
Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.
Please be careful converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).

Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:

The first is the loan principal.
The second is the monthly payment.
The next is the number of monthly payments.
The last is the loan interest.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

Example 1

What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> n
Enter the loan principal:
> 1000000
Enter the monthly payment:
> 15000
Enter the loan interest:
> 10
It will take 8 years and 2 months to repay this loan!
Let’s take a closer look at Example 1.

You know the loan principal, the loan interest and want to calculate the number of monthly payments. What do you do?

1) You need to know the nominal interest rate. It is calculated like this:

i = \dfrac{10\%}{12 * 100\%} = 0.008333...i= 
12∗100%
10%
​
 =0.008333...

2) Now you can calculate the number of months:

n = \log_{1 + 0.008333...} \left( \dfrac{15000}{15000-0.008333... * 1000000} \right) = 97.71...n=log 
1+0.008333...
​
 ( 
15000−0.008333...∗1000000
15000
​
 )=97.71...

3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and in the 98th month the user will pay 0.71... of the monthly payment. So, there are 98 months to pay.

n = 98n=98

4) Finally, you need to convert “98 months” to “8 years and 2 months” so that it is more readable and understandable for the user.

Example 2

What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> a
Enter the loan principal:
> 1000000
Enter the number of periods:
> 60
Enter the loan interest:
> 10
Your monthly payment = 21248!
Example 3

What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> p
Enter the annuity payment:
> 8721.8
Enter the number of periods:
> 120
Enter the loan interest:
> 5.6
Your loan principal = 800000!
'''
import math

a = input("""
 What do you want to calculate?
type \"n\" for number of monthly payments,
type \"a\" for annuity monthly payment amount,
type \"p\" for loan principal:
""")

if a == 'n':
    p = int(input("Enter the loan principal:"))
    m = int(input("Enter the monthly payment:")) # month payment
    i = float(input("Enter the loan interest:"))/100/12
    month = math.ceil(math.log(m/(m-i*p),i+1))
    years = month // 12
    month = month % 12
    if years == 0:
        print(f'It will take {month} months to repay this loan!')
    elif month == 0:
        print(f'It will take {years} years to repay this loan!')
    else:
        print(f'It will take {years} years and *{month} months to repay this loan!')

if a == 'a':
    p = int(input("Enter the loan principal:"))
    n = int(input("Enter the number of periods:")) # months number
    i = float(input("Enter the loan interest:"))/(100*12)
    payment = math.ceil(p*i*(1+i)**n/((1+i)**n-1)) #month payment
    print(f'Your monthly payment = {payment}!')

if a == 'p':
    a_n = float(input("Enter the annuity payment:"))
    n = int(input("Enter the number of periods:")) # month number
    i = float(input("Enter the loan interest:"))/100/12
    p = math.ceil(a_n/(i*(1+i)**n/((1+i)**n-1)))
    print(f'Your loan principal = {p}!')
    
    
\\

import math
print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
def Months(loan_principle, monthly_payment, loan_interest):
  i = loan_interest/1200
  months = math.ceil(math.log(monthly_payment/(monthly_payment - i * loan_principle), 1+i))
  return months

def Loan_principle(annuity_payment, number_of_periods, loan_interest):
  i = loan_interest/1200
  loan_principle =  annuity_payment / ((i * (1+i)**number_of_periods) / ((1 + i)**number_of_periods - 1))
  return loan_principle
    
def Monthly_payment(loan_principle, number_of_periods, loan_interest):
  i = loan_interest/1200
  monthly_payment = loan_principle * ((i * (1+i)**number_of_periods) / ((1 + i)**number_of_periods - 1))
  return monthly_payment
    
choice = input()
if choice == "n":
    print("Enter the loan principal:")
    loan_principle = float(input())
    print("Enter the monthly payment:")
    monthly_payment = float(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    mon = Months(loan_principle, monthly_payment, loan_interest)
    if mon // 12 == 0 or mon < 12:
        print(f"It will take {mon} months to repay this loan!")
    elif mon % 12 == 0 and mon // 12 == 1:
        print(f"It will take {mon // 12} year to repay this loan!")
    elif mon % 12 == 0 and mon // 12 != 1:
        print(f"It will take {mon // 12} years to repay this loan!")   
    else:
        print(f"It will take {mon // 12} years and {mon % 12} months to repay this loan!")
elif choice == "p":
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    number_of_periods = float(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    f = Loan_principle(annuity_payment,number_of_periods,loan_interest)
    print(f"Your loan principal = {math.ceil(f)}!")
elif choice == "a":
    print("Enter the loan principal:")
    loan_principle = float(input())
    print("Enter the number of periods:")
    number_of_periods = float(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    c = Monthly_payment(loan_principle, number_of_periods, loan_interest)
    print(f"Your monthly payment = {math.ceil(c)}!")

    
    
    


