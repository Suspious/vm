from youtubeposter import YoutubePoster
#add instagram
#add tiktok
# use all the files in a folder
# add cron jobs
# add time stamps
from instabot import Bot
import os
from TikTokApi import TikTokApi
import asyncio
import os
CLIENT_SECRETS_FILE = ""
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CREDENTIALS_FILE = "youtube-python-upload-credentials.json"


youtube = YoutubePoster.get_authenticated_service(CLIENT_SECRETS_FILE, SCOPES, CREDENTIALS_FILE)

YoutubePoster.initialize_upload(youtube, 'Cooledits.mp4')



bot = Bot()

bot.login(username="disciplineluxurymotivation", password="jorson192@")
for filename in os.listdir('.'):
    if filename.endswith('.mp4'):
        # Do something with the video file
        print(f'Found video file: {filename}')
        bot.upload_video(filename,caption="Like and follow")


ms_token = os.environ.get("ms_token", None) # get your own ms_token from your cookies on tiktok.com



##npm install pierreminiggio/tiktok-poster
##Utilisation :
#
#const post = require('@pierreminiggio/tiktok-poster')
#post(login, password, video, legend, show).then(() => {
#                                                      // done
#}).catch((err) => {
#    console.log(err) // 'timed out'
#})