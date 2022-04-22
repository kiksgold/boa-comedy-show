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
    while True:
        print("Please enter the ticket numbers from the last event.")
        print("Data should be three numbers, separated by commas.")
        print("Example: 60,80,30\n")

        num_str = input("Enter your numbers here: ")

        ticket_num = num_str.split(",")

        if validate_num(ticket_num):
            print('Valid Numbers')
            break

    return ticket_num


def validate_num(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_ticket_worksheet(num):
    """
    Update ticket worksheet, add new row with the numbers provided"
    '"""
    print('Updating ticket worksheet...\n')
    ticket_worksheet = SHEET.worksheet(('ticket'))
    ticket_worksheet.append_row(num)
    print('Ticket worksheet updated successfully.\n')


num = get_ticket_num()
ticket_num = [int(fig) for fig in num]
update_ticket_worksheet(ticket_num)








