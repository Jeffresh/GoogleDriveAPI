from googleapiclient.discovery import build

from auth import auth
from apigoogledrive import apidrive

if __name__ == '__main__':

    GD = apidrive.GoogleDriveV3('https://www.googleapis.com/auth/drive')


    # GD.create_file('nopath')
    #
    # GD.create_directory('nopath')


    print(GD.SCOPES)

    print(GD.search('My Report'))

    # GD.list_files()
