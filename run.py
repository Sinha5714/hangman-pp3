# Imports
# Python
# --------------------
import random
import time
import os

# 3rd Party
# --------------------
from colorama import Fore

# Internal
# --------------------
from gsheet import update_login_data
from gsheet import login_data
from gsheet import validate_user_details
# ----------------------

current_user = {'name': 'Remo'}
# A list of words from which the random words will be chose for the game
words = ['flower', 'nurse', 'house', 'packet', 'rather', 'zebra',
         'human', 'table', 'laptop', 'rating', 'notice', 'abroad',
         'accept', 'bridge', 'bamboo', 'escape',  'excess', 'guitar',
         'hunter', 'health', 'jumble', 'kitten',
         'legacy', 'notice', 'radius', 'online']


def head():
    """
    Function to display head of the game
    """
    print(Fore.RED + "================================================")
    time.sleep(1)
    print(Fore.GREEN + "||   ||   // \\  ||\\  || ||¯¯¯¯    ||========= ")
    print(Fore.GREEN + "||===||  //===\\ || \\ || ||  ||=|| ||      | ")
    print(Fore.GREEN + "||   || //     \\||  \\|| ||__|| || ||      |")
    time.sleep(1.5)
    print(Fore.GREEN + "==================================||      O ")
    print(Fore.GREEN + "   ||\\  //||  // \\  ||\\  ||       ||     /|\\ ")
    print(Fore.GREEN + "   || \\// || //===\\ || \\ ||       ||     / \\ ")
    print(Fore.GREEN + "   ||     ||//     \\||  \\||       ||==== ")
    time.sleep(1)
    print(Fore.RED + "================================================")


def signup_check():
    """
    To ask user if they already are signed up if not it promts them
    to signup and if already signed up ask them to login
    """
    exist_check = input(f"{Fore.CYAN}Are you an existing user? Y/N\n")
    if exist_check.upper() == "Y":
        user_exist()
    elif exist_check.upper() == "N":
        get_user_details()
    else:
        print(f"{Fore.RED}Invalid Input. Type Y/N")
        time.sleep(1)
        signup_check()


def get_user_details():
    """
    To get the user detail for sign up and validate
    the input provided and after validation, append the input
    to google spread worksheet
    """
    time.sleep(2)
    print(f"{Fore.GREEN}\nSIGN UP HERE!!!")
    time.sleep(2)
    print(f"{Fore.YELLOW}\nInstructions for Signup:-")
    time.sleep(1)
    print("\nUsername and Password are case sensitive")
    print("Username and Password should be more than 4 characters")
    time.sleep(1)
    user_input = input(f"{Fore.CYAN}\nEnter New Username:\n")
    time.sleep(1)
    user_password = input(f"{Fore.CYAN}\nEnter New Password: \n")
    time.sleep(2)
    validate = validate_user_details(user_input, user_password)
    if validate:
        login = [user_input, user_password]
        update_login_data(login)
        time.sleep(2)
        os.system('clear')
        user_exist()
    else:
        time.sleep(2)
        get_user_details()


def user_exist():
    """
    To check if user already exist and validate it by comparing
    the input matches in stored values in google spread worksheet
    """
    time.sleep(1)
    print(f"{Fore.GREEN}\nLOGIN TO PLAY HANGMAN!!!")
    time.sleep(1)
    username = input(Fore.CYAN + "\nUsername: \n")
    time.sleep(1)
    password = input(Fore.CYAN + "\nPassword: \n")
    logins = login_data()
    check_login = 0
    for data in logins:
        if username == data['USERNAME']:
            if password == data['PASSWORD']:
                print("\nLogged in Sucessfully...")
                time.sleep(2)
                os.system('clear')
                head()
                current_user['name'] = data['USERNAME']
                print(f"{Fore.GREEN}\nWelcome back {current_user['name']}")
            else:
                print("Incorrect password...")
                signup_check()
        else:
            check_login += 1
    if check_login == len(logins):
        print("User do not exist.Try again")
        signup_check()


def choose_random_word():
    """
    Select random word from list words and return in upper case
    """
    random_word = random.choice(words)
    return random_word.upper()


def open_rules():
    """
    Contains a while loop to ask question to open rules
    If player do not want to see the rules its automatically
    starts the game
    """
    while True:
        show_rules = input(Fore.CYAN + "\nWant to open Rules: Y/N \n")
        if show_rules.isalpha() and show_rules.upper() == "Y":
            print(f"{Fore.GREEN}\nLoading Rules......")
            time.sleep(2)
            how_to_play()
            os.system('clear')
            break
        elif show_rules.upper() == "N":
            print(f"{Fore.GREEN}\nStarting Game....\n")
            time.sleep(2)
            os.system('clear')
            break
        else:
            print(f"{Fore.RED}\nInvalid input. Please enter Y or N\n")


def how_to_play():
    """
    To display rules of the game to the user
    """
    print(f"{Fore.CYAN}\nHOW TO PLAY:-")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}Goal: guess the word and save the man!")
    time.sleep(1)
    print(f"{Fore.YELLOW}\nEverytime you can type only one letter.")
    time.sleep(1)
    print(f"{Fore.YELLOW}\nFor increasing chances of winning:")
    print(f"{Fore.YELLOW}letters 'AEIOU' is already provided ")
    print(f"{Fore.YELLOW}But hints will be provided after first guess")
    time.sleep(1)
    print(f"{Fore.YELLOW}\nMake 6 wrong guesses and you lose.")
    time.sleep(1)
    print(f"{Fore.YELLOW}\nThe man will die!")
    time.sleep(4)
    print(Fore.GREEN + "\nLet's Play!!!!")
    time.sleep(2)


def play_hangman(random_word):
    """
    Function for the game which inherit randomWord from randomWord function
    and run a while loop until no tries left. The function displays the game
    as the loop runs and validates if inputs by user is wrong and prompt
    users of the errors
    """
    guessed_letters = "AEIOU"
    tries = 6
    print(Fore.WHITE + display_hangman(tries))
    print(f"{Fore.RED}\n Total Attempts: {tries}\n")
    print(" _ " * 6)

    while tries > 0:
        wrong_letter_count = 0
        guess = input(f"{Fore.YELLOW}\n\n Please enter your guess: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{Fore.YELLOW}\n{guess} is already guessed!")
                print(Fore.WHITE + display_hangman(tries))
                print(f"{Fore.RED}\n Attempt left: {tries}\n")
            elif guess not in random_word:
                print(f"{Fore.RED}\n You guessed wrong. Try Again")
                tries -= 1
                guessed_letters += guess
                print(Fore.WHITE + display_hangman(tries))
                print(f"{Fore.RED}\n Attempt left: {tries}\n")
            else:
                print(f"{Fore.GREEN}\n Correct! {guess} is in the word.")
                print(Fore.WHITE + display_hangman(tries))
                print(f"{Fore.RED}\n Attempt left: {tries}\n")
        else:
            print(Fore.RED + "\n Invalid input. Enter only one alphabet")
            print(Fore.WHITE + display_hangman(tries))
            print(f"{Fore.RED}\n Attempt left: {tries}\n")
        guessed_letters += guess

        for letter in random_word:
            if letter in guessed_letters:
                print(f"{Fore.GREEN}{letter}", end=' ')
            else:
                print(Fore.RED + " _ ", end=' ')
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            print(f"{Fore.GREEN}\nCongrats. The secret word is {random_word}.")
            print("\nYou saved the man:)")
            break
        if tries == 0:
            print("\n")
            print(f"{Fore.GREEN}LOSER! The secret word was {random_word}.\n")

    return tries


def display_hangman(tries):
    """
    Function to display various stages of hangman game. It consist of array
    holding different stages and will be dependent on the tries.
    """
    stages = [
        """
        +----+
        |    O
        |   /|\\
        |   / \\
        ===
        """,
        """
        +----+
        |    O
        |   /|\\
        |   /
        ===
        """,
        """
        +----+
        |    O
        |   /|\\
        |
        ===
        """,
        """
        +----+
        |    O
        |   /|
        |
        ===
        """,
        """
        +----+
        |    O
        |    |
        |
        ===
        """,
        """
        +----+
        |    O
        |
        |
        ===
        """,
        """
        +----+
        |
        |
        |
        ===
        """]
    return stages[tries]


def restart_game():
    """
    Function to ask user if they want to play again
    and restart the game and if not exit the terminal
    """
    while True:
        answer = input(f"{Fore.CYAN}\nDo you want to play again?: Y/N\n")
        os.system('clear')
        if answer.upper() == "Y":
            print(f"{Fore.CYAN}\nTRY YOUR LUCK AGAIN!!")
            print(f"{Fore.GREEN}\nRestarting Game......")
            time.sleep(2.5)
            play_hangman(choose_random_word())
        elif answer.upper() == "N":
            time.sleep(1.5)
            print(f"{Fore.LIGHTCYAN_EX}\nGood Bye!!")
            time.sleep(1.5)
            print(f"{Fore.LIGHTCYAN_EX}\nLogging Out....")
            time.sleep(3)
            break
        else:
            print(f"{Fore.RED}Invalid input. Type Y/N")


def main_game():
    """
    Function to call all functions
    """
    head()
    signup_check()
    open_rules()
    play_hangman(choose_random_word())
    restart_game()


main_game()
