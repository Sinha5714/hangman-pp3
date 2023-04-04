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
    return users_login
    
def update_login_data(data):
    """
    Update users worksheet with new username and
    password data
    """
    print("Updating worksheet")
    USERS.append_row(data)
    print(" updated successfully....")   
