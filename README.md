# Loan-Calculator

Loan Calculator
This is a command-line tool written in Python that can help you calculate different types of loan payments. It can calculate annuity payments, loan periods, and differentiated payments. It takes input from the user through the command line and provides the result accordingly.

Prerequisites
Python 3.x installed on your computer
Basic knowledge of using the command line
How to Use
Running the Program
Download the loan_calculator.py file and save it in a directory on your computer.
Open the command line or terminal and navigate to the directory where the file is saved.
Type the following command to run the program:
Copy code
python loan_calculator.py
Command-Line Arguments
The program takes the following command-line arguments:

--type: This argument is required and should be either annuity or diff. If it's diff, the program will calculate differentiated payments. If it's annuity, the program will calculate the annuity payment, loan principal, or the loan periods.
--principal: The loan principal amount. This argument is required for annuity and diff types.
--periods: The number of months needed to repay the loan. This argument is required for annuity and diff types.
--interest: The annual interest rate, without the percent sign. This argument is required for all types.
--payment: The monthly payment amount. This argument is required only for the annuity type.
Examples
To calculate the differentiated payments for a loan of 100000 over 10 months at an annual interest rate of 10%, run the following command:

Copy code
python loan_calculator.py --type diff --principal 100000 --periods 10 --interest 10
To calculate the annuity payment for a loan of 100000 over 120 months at an annual interest rate of 10%, run the following command:

Copy code
python loan_calculator.py --type annuity --principal 100000 --periods 120 --interest 10
To calculate the loan principal for a monthly payment of 10000 over 10 years at an annual interest rate of 10%, run the following command:

Copy code
python loan_calculator.py --type annuity --payment 10000 --periods 120 --interest 10
To calculate the loan periods for a loan of 500000 with a monthly payment of 25000 at an annual interest rate of 10%, run the following command:

Copy code
python loan_calculator.py --type annuity --principal 500000 --payment 25000 --interest 10
