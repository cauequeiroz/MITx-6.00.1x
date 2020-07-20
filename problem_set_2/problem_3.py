# Variables
balance = 320000
annualInterestRate = 0.2

# Algorithm -Bisection Search
def calculate_final_balance(balance, annualInterestRate, minimum_payment):
    unpaid_balance = balance - minimum_payment
    interest = (annualInterestRate/12.0) * unpaid_balance

    for month in range(12):
        balance = unpaid_balance + interest
        unpaid_balance = balance - minimum_payment
        interest = (annualInterestRate/12.0) * unpaid_balance

    return round(balance, 2)

minimum_guess = balance / 12
maximum_guess = (balance * (1 + annualInterestRate/12.0)**12) / 12.0
epsilon = 0.1

while True:
    payment = round((minimum_guess + maximum_guess) / 2, 2)
    final_balance = calculate_final_balance(balance, annualInterestRate, payment)

    if abs(final_balance) <= epsilon:
        break
    elif final_balance < 0:
        maximum_guess = payment
    elif final_balance > 0:
        minimum_guess = payment

print('Lowest Payment:', payment)