# Variables
balance = 3926
annualInterestRate = 0.2

# Algorithm - Guess and Check
def calculate_final_balance(balance, annualInterestRate, payment):
    minimum_payment = payment
    unpaid_balance = balance - minimum_payment
    interest = (annualInterestRate/12.0) * unpaid_balance

    for month in range(12):
        balance = unpaid_balance + interest
        minimum_payment = payment
        unpaid_balance = balance - minimum_payment
        interest = (annualInterestRate/12.0) * unpaid_balance

    return round(balance, 2)

payment = 10

while calculate_final_balance(balance, annualInterestRate, payment) > 0:
    payment += 10

print('Lowest Payment:', payment)