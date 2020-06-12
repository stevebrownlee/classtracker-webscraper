from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from Student import Student

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


# The ID and range of a sample spreadsheet.
PROFILE_SPREADSHEET_ID = '1jlxGp0OINxtPsVrabffEP54ysRnHlhCi4CB2ZX1iwH8'
RANGE_NAME = 'Profiles!B2:E'

def get_student_names():
    names = []
    with open('students.txt', 'rb') as studentNames:
        students = studentNames.readlines()

        for student in students:
            names.append(str(student).split("\\n")[0].split("b'")[1])

    return names


def get_profiles():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('sheets.token.pickle'):
        with open('sheets.token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'sheets.credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('sheets.token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=PROFILE_SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    student_profiles = []
    allNames = get_student_names()

    if not values:
        print('No data found.')
    else:
        for row in values:
            studentName = row[0]
            replit_profile = row[2]
            codecademy_profile = row[3]


            if studentName in allNames:
                student = Student()
                student.name = studentName
                student.date_submitted = row[1]
                student.replit_profile = replit_profile
                student.codecademy_profile = codecademy_profile

                student_profiles.append(student)

    return student_profiles
