import gspread
from google.oauth2.service_account import Credentials

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
RESULT = SHEET.worksheet('result')


def login_data():
    """
    Gets login data from the player and adds it to the users worksheet
    """
    user_login = USERS.get_all_values()
    return user_login


def user_result():
    """
    Gets user results and adds to the result worksheet
    """
    result = RESULT.get_all_values()
    return result 

def get_user_details():
    """
    To get username for the game
    """
    user_login = input("Enter your username:\n")
    user_password = input("Enter your password:\n")
    print(user_login)
    print(user_password)


get_user_details()
