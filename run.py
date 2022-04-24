import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('boa-comedy-show')

def get_ticket_data():
    """
    Get ticket data input in figure from the user
    """
    while True:
        print("Please enter the ticket data from the last event.")
        print("Data should be three numbers, separated by commas.")
        print("Example: 60,80,30\n")

        data_str = input("Please enter your ticket_data here: ")

        ticket_data = data_str.split(",")

        if validate_data(ticket_data):
            print('Valid Data')
            break

    return ticket_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into integer,
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


def update_ticket_worksheet(data):
    """
    Update ticket worksheet, add new row with the data provided"
    '"""
    print('Updating ticket worksheet...\n')
    ticket_worksheet = SHEET.worksheet(('ticket'))
    ticket_worksheet.append_row(data)
    print('Ticket worksheet updated successfully.\n')


def calculate_unsold_data(ticket_row):
    """
    We will compare the ticket sales with the inventory in order to calculate the unsold(if any) of the categories
    """
    print('Calculating unsold tickets...\n')
    inventory = SHEET.worksheet('inventory').get_all_values()
    inventory_row = inventory[-1]
    print(inventory_row)




def master():
    """
    Run all our functions here
    """
    data = get_ticket_data()
    ticket_data = [int(fig) for fig in data]
    update_ticket_worksheet(ticket_data)
    calculate_unsold_data(ticket_data)


print('Welcome to BOA Comedy Show Automation')
master()








