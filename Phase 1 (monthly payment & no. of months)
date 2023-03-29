loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)

import math

print("Enter the loan principal:")
P = input() #loan principle

print('What do you want to calculate?')
print('type "n" - for number of monthly payments,')
print('type "q" - for the monthly payment:')
button = input()

if button == 'n':
    print("Enter the monthly payment:")
    monthly_payment = float(input())
    no_of_months =  math.ceil(P / monthly_payment)
    last_payment = P - (no_of_months - 1) * monthly_payment
    if last_payment > 0:
        result = f"It will take {no_of_months} months to repay the loan\nYour last payment is {round(last_payment)}."
    else:
        result = f"It will take {no_of_months} months to repay the loan"
elif button == 'q':
    print('Enter the number of months:')
    months = int(input())
    payment = P / months
    last_payment = P - (months - 1) * math.ceil(payment)
    result = f"Your monthly payment = {math.ceil(payment)}\n"
    if last_payment > 0:
        result += f"And your last payment = {round(last_payment)}."
else:
    result = "Invalid input. Please try again."

print(result)
