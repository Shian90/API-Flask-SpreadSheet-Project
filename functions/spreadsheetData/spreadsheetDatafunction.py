from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account


def spreadsheetData():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    # Take as user input?
    SAMPLE_SPREADSHEET_ID = '1XvcXPr3MLvU4RolxGlbU_0GOBYUYp-TxnIMToQaoYYQ'
    SAMPLE_RANGE_NAME = 'Orders (Form)!A1:Z1000'

    # just need to redefine this
    SERVICE_ACCOUNT_FILE = 'cherie-notebook-cred.json'
    credentials = None

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    return result
