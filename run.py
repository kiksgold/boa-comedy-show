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

def get_ticket_data():
    """
    Get ticket data input in figure from the user
    """
    while True:
        print("Please enter the ticket data from the last event.")
        print("Data should be three numbers, separated by commas.")
        print("Example: 60,80,30\n")

        data_str = input("Please enter your ticket_data here:\n")

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
    
    unsold_data = []
    for inventory, ticket in zip(inventory_row, ticket_row):
        unsold = int(inventory) - ticket
        unsold_data.append(unsold)

    return unsold_data

def update_unsold_worksheet(data):
    """
    Update unsold worksheet and add new row with the data provided
    """
    print("Updating unsold worksheet...\n")
    unsold_worksheet = SHEET.worksheet("unsold")
    unsold_worksheet.append_row(data)
    print("Unsold worksheet updated successfully.\n")

def get_last_3_entries_ticket():
    """
    Collects columns of data from ticket worksheet, collecting
    the last 3 entries for each event and returns the data
    as a list of lists.
    """
    ticket = SHEET.worksheet("ticket")
   

    columns = []
    for ind in range(1, 4):
        column = ticket.col_values(ind)
        columns.append(column[-3:])

    return columns


def calculate_inventory_data(data):
    """
    Calculate the average inventory for each item type, adding 20%
    """

    print('Calculating inventory data...\n')
    new_inventory_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        inventory_num = average * 1.2
        new_inventory_data.append(round(inventory_num))

    return new_inventory_data


def update_inventory_worksheet(data):
    """
    Update inventory worksheet and add new row with the data provided
    """
    print("Updating inventory worksheet...\n")
    inventory_worksheet = SHEET.worksheet("inventory")
    inventory_worksheet.append_row(data)
    print("Inventory worksheet updated successfully.\n")

def get_inventory_values(data):
    """
    Print out calculates average numbers for each category of tickets
    """
    headings = SHEET.worksheet('inventory').get_all_values()[0]

    print('Make the following numbers of tickets for each category for the next event:\n')

    return {heading: data for heading, data in zip(headings, data)}



def master():
    """
    Run all our functions here
    """
    data = get_ticket_data()
    ticket_data = [int(fig) for fig in data]
    update_ticket_worksheet(ticket_data)
    new_unsold_data = calculate_unsold_data(ticket_data)
    update_unsold_worksheet(new_unsold_data)
    ticket_columns = get_last_3_entries_ticket()
    inventory_data = calculate_inventory_data(ticket_columns)
    update_inventory_worksheet(inventory_data)
    inventory_values = get_inventory_values(inventory_data)
    print(inventory_values)


    


print('Welcome to BOA Comedy Show Automation')
master()








