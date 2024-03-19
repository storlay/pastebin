import io
import os

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.environ.get('DRIVE_SERVICE_ACCOUNT')
PARENT_FOLDER_ID = os.environ.get('DRIVE_FOLDER_ID')

CREDS = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)
SERVICE = build('drive', 'v3', credentials=CREDS)


def upload_message(file: str):
    """Uploading a message to Google Drive"""
    file_metadata = {
        'name': file,
        'parents': [PARENT_FOLDER_ID]
    }

    file_object = (SERVICE.files()
                   .create(body=file_metadata, media_body=file)
                   .execute())
    return file_object.get('id')


def download_message(message_id: str):
    """Downloading a message from Google Drive"""
    request = SERVICE.files().get_media(fileId=message_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    return file.getvalue().decode('utf-8')


def delete_message(message_id: str):
    """Delete a message from Google Drive"""
    SERVICE.files().delete(fileId=message_id).execute()
