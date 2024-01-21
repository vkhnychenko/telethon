from datetime import datetime

from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from apiclient import discovery as client_discovery
# from loguru import logger

from config import CREDENTIALS_FILE, SPREADSHEET_ID


credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = client_discovery.build('sheets', 'v4', http=httpAuth)


def create_sheets():
    spreadsheet = {
        'properties': {
            'title': '25-02-2022'
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))


def add_list(title: str):
    result = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=
        {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": title,
                            "gridProperties": {
                                "rowCount": 300,
                                "columnCount": 12
                            }
                        }
                    }
                }
            ]
        }).execute()
    print(result)


def append_data(list_name: str, data: list):
    body = {
        'values': [data]
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{list_name}!A1:D1",
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()

    print(result)


if __name__ == '__main__':
    try:
        # add_list('dsdd')
        # date = datetime.now().strftime('%d.%m.%Y')
        # print(date)
        append_data('test', [1, 2, 3, 4])
        # append_data('finance', [1, 2, 4, 5, 32, 1])
    except HttpError as e:
        print(e)