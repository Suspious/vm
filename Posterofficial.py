from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import json
# Replace these values with your client secrets file path and YouTube channel IDs
CLIENT_SECRETS_FILE = 'client_secret_1081709954592-0h41mo128no0ab36j1c57ipl0lnq8gb7.apps.googleusercontent.com.json'
CHANNEL_IDS = ['UCJ4zyEXT0m8NGa9ltrx7rzA', 'UCf5-XjLTggbegFN0L7_N3zA']
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDENTIALS_FILE = "youtube-python-upload-credentials.json"
import os.path
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Replace these values with your client secrets file path


def get_authenticated_service(client_secrets_file, credentials_file):
    credentials = None

    # Check if credentials file exists
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as f:
            credentials_data = json.load(f)

        # Check if the loaded data is a string and convert it to a dictionary
        if isinstance(credentials_data, str):
            credentials_data = json.loads(credentials_data)

        credentials = Credentials.from_authorized_user_info(credentials_data)

    # If credentials don't exist or are invalid, perform OAuth 2.0 flow
    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
        credentials = flow.run_local_server(port=0)

        # Save credentials for future use
        with open(credentials_file, 'w') as f:
            json.dump(credentials.to_json(), f)

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

def upload_short(video_path, title, description, youtube, channel_id):
    request = youtube.videos().insert(
        part='snippet',
        body={
            'snippet': {
                'title': title,
                'description': description,
            }
        },
        media_body=video_path
    )

    response = request.execute()
    print(f"Video uploaded successfully to channel {channel_id}. Video ID: {response['id']}")

if __name__ == '__main__':
    video_path = 'C:/Users/antho/IdeaProjects/Money machine/Cooledits.mp4'  # Replace with the path to your video file
    title = 'Join our family! Hit subscribe and lets share this journey together'
    description = '#SubscribeNow#LikeAndSubscribe#fun'

    youtube = get_authenticated_service(CLIENT_SECRETS_FILE, CREDENTIALS_FILE)
    channel_ids = 'UCf5-XjLTggbegFN0L7_N3zA','UCJ4zyEXT0m8NGa9ltrx7rzA'

    if channel_ids:
        print("Channel IDs associated with the authenticated user:")
        for channel_id in channel_ids:
            print(channel_id)

            # Replace 'your_channel_id' with the actual channel ID where you want to upload the video
            upload_short(video_path, title, description, youtube,channel_id)
    else:
        print("No channels found.")
