# Variables
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Algorithm
minimum_payment = balance * monthlyPaymentRate
unpaid_balance = balance - minimum_payment
interest = (annualInterestRate/12.0) * unpaid_balance

for month in range(12):
    balance = unpaid_balance + interest
    minimum_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - minimum_payment
    interest = (annualInterestRate/12.0) * unpaid_balance

print('Remaining balance:', round(balance, 2)) 