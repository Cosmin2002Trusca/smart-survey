import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('smart_survey')


def get_name_data():
    """
    Get name from survey subjects
    """
    print("Please enter your full name")
    print("Example: Jack Johnson\n")

    data_name = input("Enter your full name here: ")
    print(f"The name provided is {data_name}")


get_name_data()