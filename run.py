import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('smart_survey')



def is_valid_name(name):
    """
    Validates that the name is properly formatted.
    A valid name consists of at least two words with alphabetic characters.
    """
    return bool(re.match(r"^[A-Za-z]+ [A-Za-z]+$", name))

def is_valid_answer(answer):
    """
    Validates that the answer is either 'yes' or 'no'.
    """
    return answer.lower() in ["yes", "no"]

def get_survey_data():
    """
    Get name and answers from survey subjects with validation.
    """
    print("Please enter your full name.")
    print("Example: Jack Johnson\n")

    while True:
        data_name = input("Enter your full name here: ")
        if is_valid_name(data_name):
            print(f"The name provided is {data_name}\n")
            break
        else:
            print("Invalid name format. Please enter your full name (first and last name).")

    questions = [
        "Do you have a hidden talent?",
        "Have you ever written a song for someone?",
        "Do you believe in extraterrestrial life?",
        "Do you believe in ghosts?",
        "Do you believe in God?",
        "Have you tried any extreme sports?",
        "Have you participated in a quiz game or competition?"
    ]

    answers = {}

    print("Please answer with 'yes' or 'no' to the following questions.")
    for question in questions:
        while True:
            answer = input(f"{question}: ")
            if is_valid_answer(answer):
                print(f"Your answer is {answer}\n")
                answers[question] = answer.lower()
                break
            else:
                print("Invalid answer. Please respond with 'yes' or 'no'.")

    return data_name, answers


get_survey_data()

