from googleapiclient.discovery import build

from auth import auth
from apigoogledrive import apidrive

if __name__ == '__main__':

    GD = apidrive.GoogleDriveV3('https://www.googleapis.com/auth/drive')

    GD.list_files()

    GD.create_file('hola')


    print(GD.SCOPES)