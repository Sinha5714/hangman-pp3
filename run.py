import random
import colorama
from colorama import Fore

print('\n-------------------------------------------------------------------------------------------------------------------------------------------')
print(Fore.GREEN +'||        ||        //\\       ||\\      ||  ||============   ||\\      //||       //\\       ||\\      ||')
print(Fore.RED +'||        ||       //  \\      || \\     ||  ||               || \\    // ||      //  \\      || \\     ||')
print(Fore.GREEN +'||        ||      //    \\     ||  \\    ||  ||               ||  \\  //  ||     //    \\     ||  \\    ||')
print(Fore.RED +'||========||     //======\\    ||   \\   ||  ||      ||====|| ||   \\//   ||    //======\\    ||   \\   ||')
print(Fore.GREEN +'||        ||    //        \\   ||    \\  ||  ||      ||    || ||         ||   //        \\   ||    \\  ||')
print(Fore.RED +'||        ||   //          \\  ||     \\ ||  ||      ||    || ||         ||  //          \\  ||     \\ ||')
print(Fore.GREEN +'||        ||  //            \\ ||      \\||  =========     || ||         || //            \\ ||      \\||')
print('\n-------------------------------------------------------------------------------------------------------------------------------------------')

 # A list of words from which the random words will be chose for the game
words = ['flower', 'nurse','house','packet','rather','zebra','human','table','laptop','rating','notice','abroad','accept','bridge','bamboo','escape','excess','guitar','hunter','health','jumble','kitten','legacy','notice','radius','online']

def randomWord():
    """
    Select random word from list words and return in upper case
    """
    randomWord = random.choice(words)
    return randomWord.upper()

def enter_name():
    """
    Function to enter the player name in alphabets only and return playerName
    """
    playerName = input(" Enter your name: " )
    while True:
        if playerName.isalpha() and len(playerName) > 3:
            print(f'Welcome {playerName}')
        else:
            print("Invalid Input. Name should only contain alphabets and must be more than three characters")
        break
def rules():
    """
    Function to display rules of the game
    """
    playerKnowledge = input("Do you want to see the rules? : y/n ")
    if playerKnowledge.isalpha():
        print("HOW TO PLAY:-")
        print("\nGoal: guess the word and save the man!")
        print("Everytime you can type only one letter.")
        print("Make 6 wrong guesses and you lose. The man will die!")
    else:
        print("Invalid input")
    

def play_hangman(randomWord):
    """
    Function for the game which inherit randomWord from randomWord function
    """
    guessed_letters = [] # List holds the letters player guessed
    tries = 6  # Total number of tries provided to player
    # Initial display of hangman
    print("\n+----+")
    print("|    ")
    print("|    ")
    print("|    ")
    print("===   ")


    