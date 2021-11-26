'''
Description
If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.

Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.

In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.

Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:

payment = \dfrac{principal}{months}=\dfrac{1000}{9} =111.11...payment= 
months
principal
​
 = 
9
1000
​
 =111.11...

Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

lastpayment =principal -(periods-1)*payment = 1000 - 8*112=104lastpayment=principal−(periods−1)∗payment=1000−8∗112=104

In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

Objectives
The behavior of your program should look like this:

Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
To perform further calculations, you'll also have to ask for the required missing value.
Finally, output the results for the user.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

Example 1

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
Example 2

Enter the loan principal:
> 1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It will take 1 month to repay the loan
Example 3

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 10

Your monthly payment = 100
Example 4

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104.
'''
import math
principal = int(input('Enter the loan principal:'))
print("""
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
""")
payment = input()
months = int(input("Enter the number of months:"))
if payment == "m":
    month = principal/months
    if months==1:
        print(f'It will take {month} month to repay the loan')
    else:
        print(f'It will take {month} months to repay the loan')
if payment == "p":
    month = math.ceil(principal/months)
    payment = principal-(months-1)*month
    print(f'Your monthly payment = {month} and the last payment = {payment}.')
    
    
\\

print("Enter the loan principal:")
loan_principal = int(input())
print('''What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:''')
x = input()
if x == "m":
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    number_of_monthly_payments = -(-1 * loan_principal // monthly_payment)
    print()
    print("It wlii take", number_of_monthly_payments, 'month' if number_of_monthly_payments == 1 else 'months', "to repay the loan")
elif x == "p":
    print("Enter the number of months:")
    number_of_months = int(input())
    division = (loan_principal % number_of_months)
    if division == 0:
        monthly_payment = int((loan_principal / number_of_months))
        print('Your monthly payment =', monthly_payment)
    else:
        monthly_payment = (loan_principal // number_of_months + 1)
        last_payment = loan_principal - (number_of_months - 1) * monthly_payment
        print()
        print('Your monthly payment =', int(monthly_payment) ,'and the last payment = ',int(last_payment))
        
\\

import math


def calc_months():
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    months = math.ceil(principal / monthly_payment)
    if months == 1:
        print(f"It will take {months} month to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")


def calc_payment():
    print("Enter the number of months:")
    months = int(input())
    payment = math.ceil(principal / months)
    last_payment = principal % payment
    if last_payment == 0:
        print(f"Your monthly payment = {payment}.")
    else:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")


print("Enter the loan principal:")
principal = int(input())

print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
t = input()

if t == "m":
    calc_months()
elif t == "p":
    calc_payment()


