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
SHEET = GSPREAD_CLIENT.open('boa-comedy-show')

def get_ticket_num():
    """
    Get ticket numbers in figure input from the user
    """
    print("Please enter the ticket numbers from the last event.")
    print("Data should be three numbers, separated by commas.")
    print("Example: 60,80,30\n")

    num_str = input("Enter your numbers here: ")
    print(f"The numbers provided are {num_str}")

get_ticket_num()



