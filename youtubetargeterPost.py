from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up OAuth credentials
flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', ['https://www.googleapis.com/auth/youtube'])
credentials = flow.run_local_server(port=8080)

# Create YouTube API service
youtube = build('youtube', 'v3', credentials=credentials)

# List channels for the authenticated user
channels_response = youtube.channels().list(part='snippet,contentDetails').execute()
channels = channels_response.get('items', [])

# Switch to a different channel (replace CHANNEL_ID)
target_channel_id = 'YOUR_TARGET_CHANNEL_ID'
credentials['channel_id'] = target_channel_id

# Now you can perform actions on the target channel
