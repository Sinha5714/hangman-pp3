"""
To import random module
"""
import random

# To import time module
import time

# To import colorama module
from colorama import Fore

print(Fore.RED + "================================================")
time.sleep(1)
print(Fore.BLUE + "||   ||   // \\  ||\\  || ||====    ||========   ")
print(Fore.BLUE + "||===||  //===\\ || \\ || ||  ||=|| ||      | ")
print(Fore.BLUE + "||   || //     \\||  \\|| ||==|| || ||      |")
time.sleep(1.5)
print(Fore.BLUE + "==================================||      O ")
print(Fore.BLUE + "   ||\\  //||  // \\  ||\\  ||       ||     /|\ ")
print(Fore.BLUE + "   || \\// || //===\\ || \\ ||       ||     /|\ ")
print(Fore.BLUE + "   ||     ||//     \\||  \\||       ||==== ")
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


def enter_name():
    """
    Asks the player for their name and logs the name in uppercase 
    and validate the name if less than 3 characters
    """
    # Loop to validate entered username
    while True:
        username = input(Fore.CYAN + "\nEnter your name: \n").upper()
        if len(username) > 3:
            print(f"{Fore.GREEN}\nWelcome {username} to the Hangman Game:)\n")
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
        show_rules = input(Fore.RED+"Open Rules: Y/N \n")
        if show_rules.isalpha() and show_rules.upper() == "Y":
            print("Loading Rules......")
            how_to_play()
            break
        elif show_rules.upper() == "N":
            print(f"{Fore.GREEN}\nStarting Game....\n")
            break
        else:
            print(f"{Fore.RED}\nInvalid input. Please enter Y or N\n")


def how_to_play():
    """
    Function to display rules of the game
    """
    print(f"{Fore.CYAN}\nHOW TO PLAY:-")
    print(f"{Fore.YELLOW}\nGoal: guess the word and save the man!")
    print(f"{Fore.YELLOW}\nEverytime you can type only one letter.")
    print(f"{Fore.YELLOW}\nMake 6 wrong guesses and you lose.")
    print(f"{Fore.YELLOW}\nThe man will die!")


def play_hangman(random_word):
    """
    Function for the game which inherit randomWord from randomWord function
    """
    word_length = " _ " * len(random_word)

    # List holds the letters player guessed
    guessed_letters = []

    # Total number of tries provided to player
    tries = 6

    # Initial display of hangman game
    print(Fore.RED + display_hangman(tries))
    print(word_length)

    # While loop which will run until the tries are over
    while tries > 0:
        # Variable counting wrong input from user
        wrong_letter_count = 0

        # Input letter provided by user and returned in uppercase
        guess = input("\n\n Please enter a letter: ").upper()

        # If/Else statement to validate the input provided by user
        if len(guess) == 1 and guess.isalpha():
            # If/Else statement to check the letter was already guessed by user
            if guess not in random_word:
                print(Fore.RED + "\n You guessed wrong. Try Again")
                # Reduce by one with each wrong guess
                tries -= 1
                print(Fore.RED + display_hangman(tries))
                print(f"{Fore.RED}\n Attempt left: {tries}")
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print(f"{Fore.YELLOW}\n{guess} is already guessed!")
                print(display_hangman(tries))
                print(f"{Fore.RED}\n Attempt left: {tries}")
            else:
                print(f"{Fore.GREEN}\n Correct! {guess} is in the word.")
                print(f"{Fore.RED}\n Attempt left: {tries}")
                print(Fore.RED + display_hangman(tries))
        else:
            print(Fore.RED + "\n Invalid input. Enter only one letter")
            print(Fore.RED + display_hangman(tries))
            print(f"{Fore.RED}\n Attempt left: {tries}")
    
        # Guess from user added in guessed_letters list
        guessed_letters.append(guess)

        # For loop to check the value of the input and print it for display
        for letter in random_word:
            if letter in guessed_letters:
                print(f"{letter}", end=' ')
            else:
                print(" _ ", end=' ')
                # Increment as the input from user is wrong
                wrong_letter_count += 1

        # If wrong_letter_count is 0. Player wins and the loop breaks
        if wrong_letter_count == 0:
            print(f"\n Well Done. The secret word was {random_word}.\n")
            print("You saved the man:)")
            break
    return tries


def display_hangman(tries):
    """
    Function to display various stages of hangman game. It consist of array
    holding different stages and will be dependent on the tries.
    """   
    stages = ["""
                +----+"
                |    O
                |   /|\ 
                |   / \ 
                ===
              """,
              """
                +----+
                |    O
                |   /|\ 
                |   /
                ===
              """,
              """
                +----+
                |    O
                |   /|\ 
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
            print("Restarting Game......")
            print("TRY YOUR LUCK AGAIN!!")
            enter_name()
            play_hangman(choose_random_word())
        elif answer.upper() == "N":
            print("Good Bye!!")
            break
        else:
            print("Invalid input. Type Y/N")
 

def main_game():
    """
    Function to call all functions
    """
    enter_name()
    play_hangman(choose_random_word())
    restart_game()


main_game()