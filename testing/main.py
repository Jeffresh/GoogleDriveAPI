from googleapiclient.discovery import build

from auth import auth
from apigoogledrive import apidrive

if __name__ == '__main__':

    GD = apidrive.GoogleDriveV3()

    GD.list_files()


    print(GD.SCOPES)