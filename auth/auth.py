from __future__ import print_function
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class AuthDecorators:
    """
    Class to encapsulate Decorators to use in the class Auth.
    """

    @staticmethod
    def remove_credentials(func):
        """
        Remove all the URIs from SCOPES
        """

        def wrapper(*args):
            if os.path.exists('../auth/token_pickle/token.pickle'):
                os.remove('../auth/token_pickle/token.pickle')

            func(*args)

        return wrapper


class Auth(AuthDecorators):
    """
    App to give authorization and return the credentials
    """

    def __init__(self, scopes='https://www.googleapis.com/auth/drive.metadata.readonly'):
        self._SCOPES = [scopes]

        print(self._SCOPES)

    @AuthDecorators.remove_credentials
    def set_credentials(self, newscopes):
        """
        Removes all the URIs from SCOPES and adds the new ones.

        :param newscopes: A set of URIS that represent the roles for the owner of the account.
        """
        self._SCOPES = newscopes[:]


    @AuthDecorators.remove_credentials
    def add_credentials(self, morescopes):
        """
        Add the new SCOPES to the old ones.

        :param morescopes: A set of URIS that represent the roles for the owner of the account.
        """

        for uri in morescopes:
            self._SCOPES.append(uri)

        if os.path.exists('../auth/token_pickle/token.pickle'):
            os.remove('../auth/token_pickle/token.pickle')

    @property
    def SCOPES(self):
        """
        Get the SCOPES

        :return SCOPES: URIs that represent the permissions.
        """
        return self._SCOPES

    def get_credentials(self):
        """
        Obtain the credentials needed to use the service of Google Drive

        :return creds: credentials needed to access to the Google Drive Service
        """

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('../auth/token_pickle/token.pickle'):
            with open('../auth/token_pickle/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '../auth/client_secret/client_secret.json', self._SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('../auth/token_pickle/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return creds
