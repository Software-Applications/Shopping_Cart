#
## SOURCE: https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/
#
from dotenv import load_dotenv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def google_sheets_data():
    
    load_dotenv()

    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
    SHEET_NAME = os.environ.get("SHEET_NAME", "products")

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    file_name = os.path.join(os.getcwd(), "google_credentials", "gcreds.json")

    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)

    client = gspread.authorize(creds)

    doc = client.open_by_key(DOCUMENT_ID)

    sheet = doc.worksheet(SHEET_NAME)

    data = sheet.get_all_records()

    return data

#breakpoint()

#print("-----------------")
#print("SPREADSHEET:", doc.title)
#print("-----------------")

''' #working  code
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("gcreds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("shopping_cart").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records
pprint(data)
'''



'''
row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

insertRow = ["hello", 5, "red", "blue"]
sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

sheet.update_cell(2,2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet
'''