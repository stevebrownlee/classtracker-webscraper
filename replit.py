from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
FUNCTION_CLASSROOM_EXERCISES = 6
ITERATION_CLASSROOM_EXERCISES = 7
CONDITIONS_CLASSROOM_EXERCISES = 5

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1XsGnNxcZ3jYaV-MvVYj615J44qY33sXSmQtydaL4iSI'
SAMPLE_RANGE_NAME = 'Student Submissions!A2:C'

def get_replit_exercises(student):
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
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    return values


def find_student_exercises(all_submitted_exercises, student):

    for row in all_submitted_exercises:
        name = row[0]
        classroom = row[1]
        exercise = row[2]

        if student.name == row[0]:
            if classroom == 'Iteration with JavaScript':
                student.iteration_exercises.add(exercise)
            if classroom == 'JavaScript Conditions':
                student.condition_exercises.add(exercise)
            if classroom == 'JavaScript Functions':
                student.function_exercises.add(exercise)

    student.function_percent = len(student.function_exercises) / FUNCTION_CLASSROOM_EXERCISES * 100
    student.iteration_percent = len(student.iteration_exercises) / ITERATION_CLASSROOM_EXERCISES * 100
    student.condition_percent = len(student.condition_exercises) / CONDITIONS_CLASSROOM_EXERCISES * 100

    return student
