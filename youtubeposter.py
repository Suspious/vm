#pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
import os

import googleapiclient
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



#'UCf5-XjLTggbegFN0L7_N3zA','UCJ4zyEXT0m8NGa9ltrx7rzA'
#UCJ4zyEXT0m8NGa9ltrx7rzA


# Replace these values with your client secrets file path
CLIENT_SECRETS_FILE = 'client_secret_1081709954592-0h41mo128no0ab36j1c57ipl0lnq8gb7.apps.googleusercontent.com.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service(client_secrets_file):
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = build(API_NAME, API_VERSION, credentials=credentials)
    return youtube

def list_channels(youtube):
    request = youtube.channels().list(
        part='id',
        mine=True
    )
    response = request.execute()

    channel_ids = [channel['id'] for channel in response.get('items', [])]
    return channel_ids

if __name__ == '__main__':
    youtube = get_authenticated_service(CLIENT_SECRETS_FILE)
    channel_ids = list_channels(youtube)

    if channel_ids:
        print("Channel IDs associated with the authenticated user:")
        for channel_id in channel_ids:
            print(channel_id)
    else:
        print("No channels found.")


