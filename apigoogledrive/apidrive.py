from googleapiclient.discovery import build

from auth import auth


class GoogleDriveV3(auth.Auth):
    """
    Class to encapsulate the services of Google Drive
    """

    def __init__(self, scopes='https://www.googleapis.com/auth/drive.metadata.readonly'):

        super().__init__(scopes)
        creds = super().get_credentials()
        self.service = build('drive', 'v3', credentials=creds)

    def list_files(self, pageSize=10, fields="nextPageToken, files(id, name)"):
        """
        List the files of your google drive Globally
        """
        # Call the Drive v3 API
        results = self.service.files().list(
            pageSize=pageSize, fields=fields).execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

    def create_directory(self):
        #TODO implement
        pass

    def create_file(self):
        #TODO implement
        pass

    def give_permissions(self):
        #TODO implement
        pass