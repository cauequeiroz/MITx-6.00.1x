print('Please think of a number between 0 and 100!')

high = 100
low = 0

while True:
    guess = int((high + low) / 2)
    print('Is your secret number ' + str(guess) + '?')

    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_input == 'c':
        break
    elif user_input == 'l':
        low = guess
    elif user_input == 'h':
        high = guess
    else: 
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was:', guess)
