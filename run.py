import random
import colorama
from colorama import Fore

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
    if playerName.isalpha():
        print(f'Welcome {playerName}')
    else:
        print("Invalid Input. Name should only be in alphabets")



def play_hangman(randomWord):
    guessed_letters = [] # List holds the letters player guessed
    tries = 6  # Total number of tries provided to player
    # Initial display of hangman
    print("\n+----+")
    print("|    ")
    print("|    ")
    print("|    ")
    print("===   ")

    while tries > 0:
        wrong_letter_count = 0
        guess = input("\n Enter the letter: ").upper()
    
        if len(guess) == 1 and guess in randomWord:
            print(f"Correct! There is one or more {guess} in the secret word.")
        elif len(guess)!=1:
            print("\n Invalid input. Enter only one alphabet")
        else:
            tries -= 1 
            print("\n You guessed wrong. Try Again")
            print(f"\n Attempt left: {tries}")
        
        guessed_letters.append(guess)

        for letter in randomWord:
            if letter in guessed_letters:
                print(f"{letter}", end = ' ')
            else:
                print("_", end = ' ')
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            print(f"\n Well Done. The secret word was {randomWord}. You saved the man:)")

            break
        
            
        if(tries == 5):
            print("\n+----+")
            print("|    O")
            print("|    ")
            print("|    ")
            print("===   ")
        elif(tries == 4):
            print("\n+----+")
            print("|    O")
            print("|    |")
            print("|    ")
            print("===   ")
        elif(tries == 3):
            print("\n+----+")
            print("|    O ")
            print("|   /| ")
            print("|     ")
            print("===    ")
        elif(tries == 2):
            print("\n+----+")
            print("|    O ")
            print("|   /|\ ")
            print("|      ")
            print("===    ")
        elif(tries == 1):
            print("\n+----+")
            print("|    O ")
            print("|   /|\ ")
            print("|   / ")
            print("===   ")
        elif(tries == 0):
            print("\n+----+")
            print("|    O ")
            print("|   /|\ ")
            print("|   / \ ")
            print("===    ")
            print("\n You killed the man. The correct word was: ", randomWord)
            

answer = "Yes"

while answer == 'Yes':
    enter_name()
    play_hangman(randomWord())
    print("\n Do you want to play again? Yes or No")
    answer = input()
    