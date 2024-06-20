import gspread
from google.oauth2.service_account import Credentials
import re

# Define the scope and credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load the credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('smart_survey')


# Define the validation functions
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
    while True:
        print("Please enter your full name.")
        print("Example: Jack Johnson\n")
        
        data_name = input("Enter your full name here: \n")
        if not is_valid_name(data_name):
            print("Invalid name format. Please enter your full name (first and last name).")
            continue
        
        print(f"The name provided is {data_name}\n")
        
        questions = [
            "Do you plan to attend college after graduating from high school?",
            "Are you interested in pursuing a career in STEM?",
            "Do you feel prepared for future job market challenges?",
            "Are you considering starting your own business?",
            "Do you believe your high school education prepared you for your career goals?",
            "Are you interested in studying or working abroad?",
            "Do you see yourself working in the same field throughout your career?"
        ]
    
        answers = {}
    
        print("Please answer with 'yes' or 'no' to the following questions.")
        for question in questions:
            while True:
                answer = input(f"{question}: \n")
                if is_valid_answer(answer):
                    print(f"Your answer is {answer}\n")
                    answers[question] = answer.lower()
                    break
                else:
                    print("Invalid answer. Please respond with 'yes' or 'no'.")
    
        update_survey_worksheet((data_name, answers))
    
        while True:
            restart_survey = input("Do you want to start over the survey? (yes/no): ").lower()
            if restart_survey in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please respond with 'yes' or 'no'.")
    
        if restart_survey == "no":
            break
    
    print("Thank you for participating in the survey!")


def update_survey_worksheet(data):
    """
    Update survey worksheet
    """
    print("Updating survey worksheet...\n")
    survey_worksheet = SHEET.worksheet("survey")

    # Convert data to a list format suitable for appending
    name, answers = data
    data_row = [name] + list(answers.values())

    survey_worksheet.append_row(data_row)
    print("Survey worksheet updated successfully\n")

    # Retrieve all responses
    all_responses = survey_worksheet.get_all_values()[1:]  # Exclude header row
    total_responses = len(all_responses)

    percentages = {}
    for i, question in enumerate(answers.keys(), start=1):
        matching_responses = sum(1 for response in all_responses if response[i].lower() == answers[question])
        percentages[question] = (matching_responses / total_responses) * 100 if total_responses > 0 else 0

    # Display the percentages
    print("Percentage of people who answered like you for each question:")
    for question, percentage in percentages.items():
        print(f"{question}: {percentage:.2f}%")


# Main function to run the survey
if __name__ == "__main__":
    get_survey_data()
