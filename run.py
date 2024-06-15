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
    print("Please enter your full name.")
    print("Example: Jack Johnson\n")

    data_name = input("Enter your full name here: ")
    print(f"The name provided is {data_name}\n")


def get_answer_data():
    """
    Get answers from survey subjects
    """
    print("Please answer with yes or no to the following questions.")
    print("Example: Do you have a hidden talent?: no\n")

    data_question_1 = input("Do you have a hidden talent?: ")
    print(f"Your answer is {data_question_1}\n")

    data_question_2 = input("Have you ever written a song for someone?: ")
    print(f"Your answer is {data_question_2}\n")

    data_question_3 = input("Do you believe in extraterrestrial life?: ")
    print(f"Your answer is {data_question_3}\n")

    data_question_4 = input("Do you believe in ghosts?: ")
    print(f"Your answer is {data_question_4}\n")

    data_question_5 = input("Do you believe in God?: ")
    print(f"Your answer is {data_question_5}\n")

    data_question_6 = input("Have you tried any extreme sports?: ")
    print(f"Your answer is {data_question_6}\n")

    data_question_7 = input("Have you participated in a quiz game or competition?: ")
    print(f"Your answer is {data_question_7}\n")



get_name_data()
get_answer_data()