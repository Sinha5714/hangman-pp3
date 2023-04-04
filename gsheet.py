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


def login_data():
    """
    Gets login data from the player and adds it to the users worksheet
    """
    users_login = USERS.get_all_records()
    print(users_login)

def get_user_details():
    """
    To get username and password for the game
    """
    print("Sign up to play Hangman Game")
    user_input = input("Enter Username:\n")
    user_password = input("Enter Password: \n")
    login = [user_input, user_password, 0]
    update_login_data(login)
    
def update_login_data(data):
    """
    Update users worksheet with new username and
    password data
    """
    print("Updating worksheet")
    USERS.append_row(data)
    print(" updated successfully....")   

def validate_user_details(user, password):
    """
    Function to check if username already exist and
    entered username and password are valid
    """
    try:
        if user == "" or password == "" or user == " " or password ==" ":
            raise ValueError(
                "You cannot submit empty field"
            )
    except ValueError as v:
        print(f"Invalid Input: {v}")
        return False
    try:
        existing_user = login_data()
        for ind in existing_user:
            if ind["USERNAME"] == user:
                raise ValueError(
                    "Username already exist"
                )
    except ValueError as e:
        print(f"Invalid Username: {e}")
        return False
    try:
        if not (isinstance(user, str) or isinstance(password, str)):
            raise TypeError(
                "Enter details in alphabets only"
            )
    except TypeError as m:
        print(f"Invalid user input: {m}")
        return False
    else:
        print("Login confirmed....")
        return True

get_user_details()
