'''
Gets the transcripts using cURL from the Youtube API web.
'''


import os
import requests
import json

# Create GOOGLE API KEY ON:
# https://console.cloud.google.com/apis/credentials
api_key = os.environ.get("GOOGLE_API_KEY")

# Get GOOGLE ACCESS TOKEN FROM:
# https://developers.google.com/oauthplayground/
access_token = os.environ.get("GOOGLE_ACCESS_TOKEN")


def get_videos_on_playlist(id, next_page_token=None):
    '''
    Gets the videos on a playlist, running for all pages.
    Returns the video Id with the most accurate estimate
    of the interviewee's name.
    '''
    videos = []

    url = "https://youtube.googleapis.com/youtube/v3/playlistItems"
    headers = {
        'Accept': 'application/json',
    }
    params = [
        ('key', api_key),
        ('playlistId', id),
        ('part', 'snippet'),
        ('maxResults', '50'),
    ]
    if next_page_token is not None:
        params.append(('pageToken', next_page_token))
    response = requests.get(url, headers=headers, params=params)

    response_json = json.loads(response.text)

    for item in response_json['items']:
        video_id = item['snippet']['resourceId']['videoId']
        interviewee = item['snippet']['title'].split(": ")[0].lower().replace(" ", "_")
        if len(interviewee) > 20:
            interviewee = interviewee[:20]
        videos.append((video_id, interviewee))

    if 'nextPageToken' in response_json:
        videos += get_videos_on_playlist(id, response_json['nextPageToken'])

    return videos


def get_captions_on_video(id):
    '''
    Gets the captions ids for a certain video.
    '''
    url = "https://youtube.googleapis.com/youtube/v3/captions"
    headers = {
        'Accept': 'application/json',
    }
    params = (
        ('key', api_key),
        ('part', 'snippet'),
        ('videoId', id)
    )
    response = requests.get(url, headers=headers, params=params)
    
    response_json = json.loads(response.text)

    return response_json['items']['id']


def download_captions(id, lang='es'):
    '''
    Downloads the captions for a certain video.
    FAILING: "Expected OAuth2 access token" but i cant find where to get it.
    '''
    url = "https://youtube.googleapis.com/youtube/v3/captions/{}".format(id)
    headers = {
        'Accept': 'application/json',
        'Authorization': access_token
    }
    params = (
        ('key', api_key),
        ('tfmt', 'srt'),
        ('tlang', lang),
        ('part', 'snippet'),
    )

    response = requests.get(url, headers=headers, params=params)

    return print(response)





if __name__ == "__main__":
    # videos = get_videos_on_playlist("PLaw1K4GjZVeOZvCiwxqBvHjUwnKFd8Jw3")
    # for v in videos:
    #    print(v[1])

    # captions = get_captions_on_video("DDXkGDFooUM")
    # print(captions)

    cd = download_captions("AUieDaarzDm-ESBmhpVrxcKZC3tSNnaAmvOIGkjauqvN_qroJWE")
    print(cd)