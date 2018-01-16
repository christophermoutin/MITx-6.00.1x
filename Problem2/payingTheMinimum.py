"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly
payment required by the credit card company each month.

The following variables contain values as described below:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, 
and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0

Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41

instead of

Remaining balance: 813.4141998135 

Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
"""

monthlyInterestRate=annualInterestRate/12.0
totalPaid=0

for i in range(1,13):
    print('Month: '+str(i))
    minMonthlyPayment=monthlyPaymentRate * balance
    print('Minimum monthly payment: '+str(round(minMonthlyPayment,2)))
    totalPaid = round(totalPaid+minMonthlyPayment,2)
    monthlyUnpaidBalance = balance-minMonthlyPayment
    balance = monthlyUnpaidBalance+monthlyUnpaidBalance*monthlyInterestRate
    if i == 12:
        print('Remaining balance: '+str(round(balance,2)))
        print('Total Paid: '+str(round(totalPaid,2)))
    print('Remaining balance: '+str(round(balance,2)))
