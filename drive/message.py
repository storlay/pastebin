"""
Downloading, uploading and deleting messages from Google Drive
"""

import io
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


class GDrive:
    SCOPES = ["https://www.googleapis.com/auth/drive"]
    SERVICE_ACCOUNT_FILE = os.environ.get("DRIVE_SERVICE_ACCOUNT")
    PARENT_FOLDER_ID = os.environ.get("DRIVE_FOLDER_ID")

    CREDS = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    SERVICE = build("drive", "v3", credentials=CREDS)

    @classmethod
    def upload(cls, file: str) -> str:
        """
        Uploading a message to Google Drive
        :param file: file name
        """
        file_metadata = {"name": file, "parents": [cls.PARENT_FOLDER_ID]}

        file_object = (
            cls.SERVICE.files()
            .create(body=file_metadata, media_body=file)
            .execute()
        )
        return file_object.get("id")

    @classmethod
    def download(cls, message_id: str) -> str:
        """
        Downloading a message from Google Drive
        :param message_id: message id
        """
        request = cls.SERVICE.files().get_media(fileId=message_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        return file.getvalue().decode("utf-8")

    @classmethod
    async def delete(cls, message_id: str) -> None:
        """
        Delete a message from Google Drive
        :param message_id: message id
        """
        cls.SERVICE.files().delete(fileId=message_id).execute()
