import random
import time
from colorama import Fore
from gsheet import validate_user_details
from gsheet import update_login_data

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

# A list of words from which the random words will be chose for the game
words = ['flower', 'nurse', 'house', 'packet', 'rather', 'zebra',
         'human', 'table', 'laptop', 'rating', 'notice', 'abroad',
         'accept', 'bridge', 'bamboo', 'escape',  'excess', 'guitar',
         'hunter', 'health', 'jumble', 'kitten',
         'legacy', 'notice', 'radius', 'online']


def choose_random_word():
    """
    Select random word from list words and return in upper case
    """
    random_word = random.choice(words)
    return random_word.upper()


def get_user_details():
    """
    To get username and password for the game
    """
    print("Sign up to play Hangman Game")
    user_input = input("Enter Username:\n")
    user_password = input("Enter Password: \n")
    login = [user_input, user_password, 0]
    update_login_data(login)


def enter_name():
    """
    Asks the player for their name and logs the name in uppercase
    and validate the name if less than 3 characters
    """
    # Loop to validate entered username
    while True:
        username = input(Fore.CYAN + "\nEnter your name: \n").upper()
        if len(username) > 3:
            time.sleep(1)
            print(f"{Fore.GREEN}\nWelcome {username} to the Hangman Game:)\n")
            time.sleep(1.5)
            open_rules()
            break
        else:
            print("Invalid input. Name should be more than 3 characters")


def open_rules():
    """
    Contains a while loop to ask question to open rules
    """
    # Loop to ask the same question if there is an error
    while True:
        show_rules = input(Fore.CYAN + "Want to open Rules: Y/N \n")
        if show_rules.isalpha() and show_rules.upper() == "Y":
            print(f"{Fore.GREEN}\nLoading Rules......")
            time.sleep(2)
            how_to_play()
            break
        elif show_rules.upper() == "N":
            print(f"{Fore.GREEN}\nStarting Game....\n")
            time.sleep(2)
            break
        else:
            print(f"{Fore.RED}\nInvalid input. Please enter Y or N\n")


def how_to_play():
    """
    Function to display rules of the game
    """
    print(f"{Fore.CYAN}\nHOW TO PLAY:-")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}Goal: guess the word and save the man!")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}\nEverytime you can type only one letter.")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}\nFor increasing chances of winning:")
    print(f"{Fore.YELLOW}letters 'AEIOU' is already provided ")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}\nMake 6 wrong guesses and you lose.")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}\nThe man will die!")
    time.sleep(4)
    print(Fore.GREEN + "\nLet's Play!!!!")
    time.sleep(2)


def play_hangman(random_word):
    """
    Function for the game which inherit randomWord from randomWord function
    """
    # List holds the letters player guessed
    guessed_letters = "AEIOU"

    # Total number of tries provided to player
    tries = 6

    # Initial display of hangman game
    print(Fore.WHITE + display_hangman(tries))
    print(f"{Fore.RED}\nAttempt left: {tries}\n")

    # While loop which will run until the tries are over
    while tries > 0:

        # Variable counting wrong input from user
        wrong_letter_count = 0

        # For loop to check the value of the input and print it for display
        for letter in random_word:
            if letter in guessed_letters:
                print(f"{Fore.GREEN}{letter}", end=' ')
            else:
                print(Fore.RED + " _ ", end=' ')
                # Increment as the input from user is wrong
                wrong_letter_count += 1

        # Input letter provided by user and returned in uppercase
        guess = input(f"{Fore.YELLOW}\n\n Please enter your guess: ").upper()

        # If/Else statement to validate the input provided by user
        if len(guess) == 1 and guess.isalpha():
            # If/Else statement to check the letter was already guessed by user
            if guess in guessed_letters:
                print(f"{Fore.YELLOW}\n{guess} is already guessed!")
                print(Fore.WHITE + display_hangman(tries))
                print(f"{Fore.RED}\n Attempt left: {tries}\n")
            elif guess not in random_word:
                print(f"{Fore.RED}\n You guessed wrong. Try Again")
                # Reduce by one with each wrong guess
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

        # Add guess to guessed letters
        guessed_letters += guess

        # If wrong_letter_count is 0. Player wins and the loop breaks
        if wrong_letter_count == 0:
            print(f"{Fore.GREEN}\nCongrats. The secret word is {random_word}.")
            print("\nYou saved the man:)")
            break
        # If tries is 0. It prints the player lost message
        elif tries == 0:
            print(f" You lose. The secret word was {random_word}.\n")

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
        answer = input("\nDo you want to play again?: Y/N\n")
        if answer.upper() == "Y":
            print(f"{Fore.CYAN}\nTRY YOUR LUCK AGAIN!!")
            print(f"{Fore.GREEN}\nRestarting Game......")
            time.sleep(2.5)
            enter_name()
            play_hangman(choose_random_word())
        elif answer.upper() == "N":
            time.sleep(1.5)
            print(f"{Fore.LIGHTCYAN_EX}\nGood Bye!!")
            break
        else:
            print("Invalid input. Type Y/N")

get_user_details()
def main_game():
    """
    Function to call all functions
    """
    
    enter_name()
    play_hangman(choose_random_word())
    restart_game()



