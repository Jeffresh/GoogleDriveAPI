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

    def _get_items(self, query=None, pagesize=None, fields="nextPageToken, files(id, name)"):
        """
        Get the items of the Google Drive
        :parameter query:
        :parameter pagesize:
        :parameter fields:
        :return items: All the objects (folders and files) of your Google Drive
        """

        results = self.service.files().list(q=query, pageSize=pagesize, fields=fields).execute()

        return results

    def list_files(self, pagesize=10, fields="nextPageToken, files(id, name)"):
        # TODO search what fields is it.
        """
        List the files of your google drive Globally
        :param pagesize: Shows the n elements. Default value = 10.
        :param fields:
        """
        response = self._get_items(None, pagesize, fields)
        items = response.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

        return items

    def create_directory(self, path, name='My Directory'):

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        file = self.service.files().create(body=file_metadata,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def create_file(self, path=None, name='My Report'):

        # TODO parametrize correctly

        # application / vnd.google - apps.document google docs
        # application/vnd.google-apps.file 	Google Drive file
        # application/vnd.google-apps.folder 	Google Drive folder
        # application/vnd.google-apps.spreadsheet 	Google Sheets

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.document'
        }

        file = self.service.files().create(body=file_metadata,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def upload_directory(self, path, name):

        # TODO implement: change mimetype for folder
        pass
        # application / vnd.google - apps.document google docs
        # application/vnd.google-apps.file 	Google Drive file
        # application/vnd.google-apps.folder 	Google Drive folder
        # application/vnd.google-apps.spreadsheet 	Google Sheets

        # file_metadata = {
        #     'name': name,
        #     'mimeType': 'application/vnd.google-apps.document'
        # }
        # media = MediaFileUpload(path,
        #                         mimetype='text/doc',
        #                         resumable=True)
        #
        # file = self.service.files().create(body=file_metadata,
        #                                     media_body=media,
        #                                     fields='id').execute()
        # print('File ID: %s' % file.get('id'))

    def upload_file(self):
        # TODO implement, change mimetype to generic upload or concrete upload by files
        # application / vnd.google - apps.document google docs
        # application/vnd.google-apps.file 	Google Drive file
        # application/vnd.google-apps.folder 	Google Drive folder
        # application/vnd.google-apps.spreadsheet 	Google Sheets

        # file_metadata = {
        #     'name': name,
        #     'mimeType': 'application/vnd.google-apps.document'
        # }
        # media = MediaFileUpload(path,
        #                         mimetype='text/doc',
        #                         resumable=True)
        #
        # file = self.service.files().create(body=file_metadata,
        #                                     media_body=media,
        #                                     fields='id').execute()
        # print('File ID: %s' % file.get('id'))
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

    def search(self, name_file):
        """
        :param name_file: name of the file to search
        :return: a dictionary of dictionaries
        """

        page_token = None

        files = []

        while True:

            response = self._get_items("name='{}'".format(name_file),page_token,
                                       'nextPageToken, files(id, name, createdTime)',
                                       )

            for file in response.get('files', []):
                files.append({'id': file.get('id'), 'name': file.get('name'), 'date_creation': file.get('createdTime')})

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

        return files
