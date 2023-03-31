# Loan-Calculator

This Calculator has the capacity to compute differentiated payments. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. 

Objectives
By the end of the final phase, I am going to implement the following features:

Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount).
The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
Handling of invalid parameters. 
The final version of this program is supposed to work from the command line and parse the following parameters:

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
