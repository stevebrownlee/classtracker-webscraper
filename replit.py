from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
VARIABLES_INTRO_CLASSROOM_EXERCISES = 7
ARRAYS_INTRO_CLASSROOM_EXERCISES = 11
OBJECTS_INTRO_CLASSROOM_EXERCISES = 7
FUNCTION_INTRO_CLASSROOM_EXERCISES = 15
FUNCTION_CLASSROOM_EXERCISES = 6
ITERATION_CLASSROOM_EXERCISES = 7
CONDITIONS_CLASSROOM_EXERCISES = 5

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1XsGnNxcZ3jYaV-MvVYj615J44qY33sXSmQtydaL4iSI'
SAMPLE_RANGE_NAME = 'Student Submissions!A2:C'


def get_replit_submissions(student):
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
    assumed_replit_name = student.name

    # Build a set of all repl.it usernames in the submissions
    replit_usernames = set()
    for row in all_submitted_exercises:
        replit_usernames.add(row[0])

    # If the name on our spreadsheet is not found in the submissions, find a likely match
    if student.name not in replit_usernames:
        print(f'NSS student {student.name} not found in repl.it submissions. Finding possible match...')
        fuzzyMatches = process.extract(student.name, replit_usernames)

        top_match_name = fuzzyMatches[0][0]
        top_match_score = fuzzyMatches[0][1]

        if top_match_score > 65:
            print(f'Best possible match is {top_match_name} with a probability of {top_match_score}%')
            assumed_replit_name = top_match_name
        else:
            print(f'No matches found. Student has no submissions. Please double check on the repl.it platform.')



    for row in all_submitted_exercises:
        replit_username = row[0]
        classroom = row[1]
        exercise = row[2]

        if assumed_replit_name == replit_username:
            if classroom == 'Iteration with JavaScript':
                student.iteration_exercises.add(exercise)
            if classroom == 'JavaScript Conditions':
                student.condition_exercises.add(exercise)
            if classroom == 'JavaScript Functions':
                student.function_exercises.add(exercise)
            if classroom == 'Introduction to Functions':
                student.functions_intro_exercises.add(exercise)
            if classroom == 'Introduction to JavaScript Variables':
                student.variables_intro_exercises.add(exercise)
            if classroom == 'Introduction to Arrays and Iteration':
                student.iteration_intro_exercises.add(exercise)
            if classroom == 'Introduction to Objects':
                student.objects_intro_exercises.add(exercise)

    student.function_percent = len(student.function_exercises) / FUNCTION_CLASSROOM_EXERCISES * 100
    student.iteration_percent = len(student.iteration_exercises) / ITERATION_CLASSROOM_EXERCISES * 100
    student.condition_percent = len(student.condition_exercises) / CONDITIONS_CLASSROOM_EXERCISES * 100

    student.intro_functions_percent = len(student.functions_intro_exercises) / FUNCTION_INTRO_CLASSROOM_EXERCISES * 100
    student.intro_iteration_percent = len(student.iteration_intro_exercises) / ARRAYS_INTRO_CLASSROOM_EXERCISES * 100
    student.intro_objects_percent = len(student.objects_intro_exercises) / OBJECTS_INTRO_CLASSROOM_EXERCISES * 100
    student.intro_variables_percent = len(student.variables_intro_exercises) / VARIABLES_INTRO_CLASSROOM_EXERCISES * 100

    return student
