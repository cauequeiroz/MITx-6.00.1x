import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()

    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in lettersGuessed:
        if letter in secretWord:
            secretWord = secretWord.replace(letter, '')  
    
    return len(secretWord) == 0

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''

    for letter in secretWord:
        guessedWord += letter if letter in lettersGuessed else '_ '

    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase

    for letter in lettersGuessed:
        available_letters = available_letters.replace(letter, '')
    
    return available_letters    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    '''
    available_guesses = 8
    letters_guessed = []    
    old_guessed_word = getGuessedWord(secretWord, letters_guessed)

    won = False
    status = ''
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord),'letters long.')

    while available_guesses > 0:        
        available_letters = getAvailableLetters(letters_guessed)
        
        print('-------------')
        print('You have', available_guesses,'guesses left.')
        print('Available letters:', available_letters)

        guess = input('Please guess a letter: ')
        guess = guess.lower()

        if guess in letters_guessed:
            status = "Oops! You've already guessed that letter:"
        else: 
            letters_guessed.append(guess)
            new_guessed_word = getGuessedWord(secretWord, letters_guessed)

            if new_guessed_word != old_guessed_word:
                status = "Good guess:"
            else:
                status = "Oops! That letter is not in my word:"
                available_guesses -= 1
                
            old_guessed_word = new_guessed_word

        print(status, new_guessed_word)

        if len(secretWord) == len(new_guessed_word):
            won = True
            break

    if won:
        status = 'Congratulations, you won!'
    else: 
        status = 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'

    print('-------------')
    print(status)

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
