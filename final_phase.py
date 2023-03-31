import argparse
import math

def diff_payment(principal, periods, interest):
    total_payment = 0
    for i in range(1, periods + 1):
        monthly_payment = math.ceil(principal / periods + interest * (principal - (principal * (i - 1)) / periods))
        total_payment += monthly_payment
        print(f"Month {i}: payment is {monthly_payment}")
    overpayment = total_payment - principal
    print(f"\nOverpayment = {overpayment}")


def annuity_payment(principal, periods, interest, payment=None):
    if payment is None:
        payment = math.ceil(principal * (interest / 1200 * pow(1 + interest / 1200, periods)) / (pow(1 + interest / 1200, periods) - 1))
        total_payment = payment * periods
        overpayment = total_payment - principal
        print(f"\nYour annuity payment = {payment}!")
        print(f"Overpayment = {overpayment}")
    else:
        x = 1 + interest / 1200
        principal = payment / ((interest / 1200) * pow(x, periods) / (pow(x, periods) - 1))
        total_payment = payment * periods
        overpayment = total_payment - principal
        print(f"\nYour credit principal = {principal:.0f}!")
        print(f"Overpayment = {overpayment:.0f}")



def loan_periods(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - interest / 1200 * principal), 1 + interest / 1200))
    total_payment = payment * periods
    overpayment = total_payment - principal
    years, months = divmod(periods, 12)
    if years == 0:
        print(f"\nIt will take {months} months to repay this loan!")
    elif months == 0:
        print(f"\nIt will take {years} years to repay this loan!")
    else:
        print(f"\nIt will take {years} years and {months} months to repay this loan!")
    print(f"Overpayment = {overpayment}")

parser = argparse.ArgumentParser(description="Loan calculator.")
parser.add_argument("--type", choices=["annuity", "diff"], help="The type of payment: 'annuity' or 'diff'.")
parser.add_argument("--principal", type=int, help="The loan principal amount.")
parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan.")
parser.add_argument("--interest", type=float, help="The interest rate per year (without the percent sign).")
parser.add_argument("--payment", type=int, help="The monthly payment amount.")

args = parser.parse_args()

if args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif not args.interest:
    print("Incorrect parameters")
else:
    nominal_interest = args.interest / 1200
    if args.type == "diff":
        overpayment = 0
        for i in range(1, args.periods + 1):
            payment = math.ceil(args.principal / args.periods + nominal_interest * (args.principal - (args.principal * (i - 1)) / args.periods))
            overpayment += payment - args.principal / args.periods
            print(f"Month {i}: payment is {payment:.0f}")
        print(f"\nOverpayment = {overpayment:.0f}")
    elif args.type == "annuity":
        if not args.payment:
            annuity_payment = math.ceil(args.principal * nominal_interest * pow(1 + nominal_interest, args.periods) / (pow(1 + nominal_interest, args.periods) - 1))
            overpayment = annuity_payment * args.periods - args.principal
            print(f"Your annuity payment = {annuity_payment:.0f}!")
            print(f"Overpayment = {overpayment:.0f}")
        elif not args.principal:
            credit_principal = args.payment / (nominal_interest * pow(1 + nominal_interest, args.periods) / (pow(1 + nominal_interest, args.periods) - 1))
            overpayment = args.payment * args.periods - credit_principal
            print(f"Your credit principal = {credit_principal:.0f}!")
            print(f"Overpayment = {overpayment:.0f}")
        elif not args.periods:
            periods = math.ceil(math.log(args.payment / (args.payment - nominal_interest * args.principal), 1 + nominal_interest))
            overpayment = args.payment * periods - args.principal
            years = periods // 12
            months = periods % 12
            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
            print(f"Overpayment = {overpayment:.0f}")
        else:
            print("Incorrect parameters")




