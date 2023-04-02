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
words = ['flower', 'nurse','house','elephant','jupiter','zebra','human','table','laptop','notebook','kitchen','abroad','accept','bridge','bamboo','escape','excess','guitar','hunter','health','jumble','kitten','legacy','notice']

def randomWord():
    """
    Select random word from list words and return in upper case
    """
    randomWord = random.choice(words)
    return randomWord.upper()

