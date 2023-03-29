
print('What do you want to calculate?')
print('type "n" for number of monthly payments,') 
print('type "a" for annuity monthly payment amount,') 
print('type "p" for loan principal:')

button = input()
def months_to_years(months):
    years = months // 12
    remaining_months = months % 12
    if years == 0:
        return f"{remaining_months} months"
    elif remaining_months == 0:
        return f"{years} years"
    else:
        return f"{years} years and {remaining_months} months"


if button == 'n':
    print("Enter the loan principal:")
    P = float(input()) #loan principle
    
    print("Enter the monthly payment:")
    A = float(input())
    
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = (loan_interest / 12) / 100
    
    n = math.ceil(math.log(A / (A - i * P), 1 + i))
    print("It will take", months_to_years(n), "to repay this loan!")
    
elif button == 'a':
    def calculate_annuity(P, loan_intrest, n):
        i = loan_intrest / (12 * 100)
        annuity = P * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        return annuity
    
    print("Enter the loan principal:")
    P = int(input())
    
    print("Enter the number of periods:")
    n = int(input())
    
    print("Enter the loan interest:")
    loan_intrest = float(input())

    annuity = math.ceil(calculate_annuity(P, loan_intrest, n))
    
    print("Your monthly payment =", annuity, "!")

elif button == 'p':
    print("Enter the annuity payment:")
    A = float(input()) #annuity_payment
    
    print("Enter the number of periods:")
    n = int(input()) #number_of_periods
    
    print("Enter the loan interest:")
    loan_interest = float(input())
    
    i = ( loan_interest / 12) / 100
    P = A * ((1 + i) ** n - 1) / (i * (1 + i) ** n)


    print("Your loan principal", P, "!")
    


