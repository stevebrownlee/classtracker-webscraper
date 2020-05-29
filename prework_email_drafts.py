# from __future__ import print_function
import pickle
import os.path
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from urllib.error import HTTPError

# delete the token.pickle file in this directory if trying to authorize a different gmail acount

# initial test data

student1 = {
  'name': 'Ryan',
  'email': 'example1@email.com'
}

student2 = {
  'name': 'Matt',
  'email': 'example2@email.com'
}

student3 = {
  'name': 'Corri',
  'email': 'example3@email.com'
}

student_obj_list = [student1, student2, student3]
student_obj_list = sorted(student_obj_list, key=lambda x: x['name'], reverse=True)

# user email settings. modify as needed

sender_name = 'NSS staff member'

email_subject_line = 'NSS Prework'

email_body = 'Insert message body here'

def message_template(student_name):
    return f'Hi {student_name},\n\n{email_body}\n\nBest regards,\n{sender_name}'

# --------------------

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  raw = base64.urlsafe_b64encode(message.as_bytes())
  raw = raw.decode()
  return {'raw': raw}

def create_draft(service, user_id, message_body):
  """Create and insert a draft email. Print the returned draft's message and id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message_body: The body of the email message, including headers.

  Returns:
    Draft object, including draft id and message meta data.
  """
  try:
    message = {'message': message_body}
    draft = service.users().drafts().create(userId=user_id, body=message).execute()

    # print('Draft id: %s\nDraft message: %s' % (draft['id'], draft['message']))

    return draft
  except HTTPError as error:
    print('An error occurred: %s' % error)
    return None

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']

def create_drafts(student_list):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    for student in student_list:
        message = create_message('me', student['email'], email_subject_line, message_template(student['name']))
        draft = create_draft(service, 'me', message)

if __name__ == '__main__':
    create_drafts(student_obj_list)