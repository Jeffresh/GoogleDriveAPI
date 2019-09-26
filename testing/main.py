from googleapiclient.discovery import build

from auth import auth
from apigoogledrive import apidrive

if __name__ == '__main__':

    GD = apidrive.GoogleDriveV3('https://www.googleapis.com/auth/drive')

    # GD.create_directory()
    # GD.create_file('New File', 'My Directory')
    # GD.create_directory('New Directory', 'My Directory')

    GD.upload_directory('UploadDirectory', 'Uploaded')

    #
    # GD.create_directory('nopath')

    print(GD.SCOPES)

    # print(GD.search('My Report'))

    # GD.share_with('My Report', 'jeff.uca@gmail.com')

    # GD.list_files()
