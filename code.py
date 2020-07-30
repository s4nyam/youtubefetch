api_key = #My_API_Key_From_Youtube #Fetch from Console.Developers.Google.com
#The Program fetches the Titles from all videos of the channel ID - UCq-Fj5jknLsUf-MWSy4_brA which is actually Tseries
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)
def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

videos = get_channel_videos('UCq-Fj5jknLsUf-MWSy4_brA')
len(videos)
for video in videos:
    print(video['snippet']['title'])
