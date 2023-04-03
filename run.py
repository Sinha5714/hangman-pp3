import random
import colorama
from colorama import Fore

print(Fore.GREEN'\n-------------------------------------------------------------------------------------------------------------------------------------------')
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

    # While loop which will run until the tries are over
    while tries > 0:
        # Variable counting wrong input from user
        wrong_letter_count = 0
        # Input letter provided by user and returned in uppercase
        guess = input("\n Please enter a letter: ").upper() 

        # If/Else statement to validate the input provided by user
        if len(guess) == 1 and guess.isalpha():
            # If/Else statement to check the letter was already guessed by user
            if guess in guessed_letters:
                print(f"You have already guessed the letter {guess}")
            elif guess not in randomWord:
                print("\n You guessed wrong. Try Again")
                tries -= 1 # Reduce by one with each wrong guess
                print(f"\n Attempt left: {tries}")
                guessed_letters.append(guess)
            else:
                print(f"Correct! There is one or more {guess} in the secret word.")         
        else:
           print("\n Invalid input. Enter only one character and it must be an alphabet")
        
        # Guess from user added in guessed_letters list
        guessed_letters.append(guess)
        
        # For loop to check the value of the input and print it for display
        for letter in randomWord:
            if letter in guessed_letters:
                print(f"{letter}", end = ' ')        
            else:
                print("_", end = ' ')
                wrong_letter_count += 1 # Increment as the input from user is wrong
        
        # If wrong_letter_count is 0. Player wins        
        if wrong_letter_count == 0:
            print(f"\n Well Done. The secret word was {randomWord}. You saved the man:)")
            break
        
            
        