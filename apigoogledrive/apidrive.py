from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from auth import auth


class GoogleDriveV3(auth.Auth):
    """
    Class to encapsulate the services of Google Drive
    """

    def __init__(self, scopes='https://www.googleapis.com/auth/drive.metadata.readonly'):

        super().__init__(scopes)
        creds = super().get_credentials()
        self.service = build('drive', 'v3', credentials=creds)

    def list_files(self, pagesize=10, fields="nextPageToken, files(id, name)"):
        """
        List the files of your google drive Globally
        """
        # Call the Drive v3 API
        results = self.service.files().list(
            pageSize=pagesize, fields=fields).execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

    def create_directory(self, path, name):
        # TODO implement
        pass

    def create_file(self, path=None, name='My Report'):

        # application / vnd.google - apps.document google docs
        # application/vnd.google-apps.file 	Google Drive file
        # application/vnd.google-apps.folder 	Google Drive folder
        # application/vnd.google-apps.spreadsheet 	Google Sheets

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.document'
        }

        file = self.service.files().create(body=file_metadata,
                                            media_body=None,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def upload_directory(self, path, name):

        # application / vnd.google - apps.document google docs
        # application/vnd.google-apps.file 	Google Drive file
        # application/vnd.google-apps.folder 	Google Drive folder
        # application/vnd.google-apps.spreadsheet 	Google Sheets

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.document'
        }
        media = MediaFileUpload(path,
                                mimetype='text/doc',
                                resumable=True)

        file = self.service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))


    def upload_file(self):
        # TODO implement
        pass

    def give_permissions(self, file, user):
        # TODO implement
        pass

    def remove_permissions(self, file, user):
        # TODO implement
        pass

    def share_with(self, file, user):
        # TODO implement
        pass
