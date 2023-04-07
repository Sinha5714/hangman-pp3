# Imports
# 3rd Party
# --------------------
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore
# ---------------------

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
    Extract data from worksheet for validation of login
    data provided by user
    """
    users_login = USERS.get_all_records()
    return users_login


def update_login_data(data):
    """
    Update users worksheet with new username and
    password data provided by user
    """
    USERS.append_row(data)


def validate_user_details(user, password):
    """
    Function to check if username already exist and
    entered username and password are valid. It also prompt an error
    to user if input provided is wrong
    """
    try:
        if len(user) < 5 or len(password) < 5:
            raise ValueError(
                "Username and Password should be more than 4 characters"
            )
    except ValueError as v:
        print(f"{Fore.RED}\nInvalid Input: {v}")
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
        print("\nSign Up confirmed....")
        return True
