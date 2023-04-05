import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_pp3')
USERS = SHEET.worksheet('users')


def login_data():
    """
    Gets login data from the player and adds it to the users worksheet
    """
    users_login = USERS.get_all_records()
    return users_login
    

def update_login_data(data):
    """
    Update users worksheet with new username and
    password data
    """ 
    USERS.append_row(data)


def validate_user_details(user, password):
    """
    Function to check if username already exist and
    entered username and password are valid
    """
    try:
        if len(user) < 5 or len(password) < 5:
            raise ValueError(
                "Username and Password should be more than 4 characters"
            )
    except ValueError as v:
        print(f"\nInvalid Input: {v}")
        return False
    try:
        existing_user = login_data()
        for ind in existing_user:
            if ind["USERNAME"] == user:
                raise ValueError(
                    "\nUsername already exist"
                )
    except ValueError as e:
        print(f"{Fore.RED}\nInvalid Username: {e}")
        return False
    try:
        if not (isinstance(user, str) or isinstance(password, str)):
            raise TypeError(
                "\nEnter details in string form only"
            )
    except TypeError as m:
        print(f"Invalid user input: {m}")
        return False
    else:
        print("\nLogin confirmed....")
        return True
