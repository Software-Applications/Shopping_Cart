# gsheets_meta.py

from dotenv import load_dotenv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def google_sheets_meta():
    
    load_dotenv()

    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
    SHEET_NAME = os.environ.get("METADATA", "meta")

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    file_name = os.path.join(os.getcwd(), "google_credentials1", "gcreds.json")

    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)

    client = gspread.authorize(creds)

    doc = client.open_by_key(DOCUMENT_ID)

    sheet = doc.worksheet(SHEET_NAME)

    data = sheet.get_all_records()

    return data