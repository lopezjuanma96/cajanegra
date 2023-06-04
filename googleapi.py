'''
Gets the videos captions using the Youtube API
Could not get this to work. The tutorial on the Youtube API website is not
up to date and raises "credentials.run_console does not exist" error.
Using this:
https://stackoverflow.com/questions/75602866/google-oauth-attributeerror-installedappflow-object-has-no-attribute-run-co
Raises error on Oauth authentication page "Request is invalid"
'''


import io
import os

import googleapiclient.discovery

from googleapiclient.http import MediaIoBaseDownload


def get_videos_on_playlist(id, next_page_token=None):
    '''
    Gets the videos on a playlist, running for all pages.
    Returns the video Id with the most accurate estimate
    of the interviewee's name.
    Could not get this to work. The tutorial on the Youtube API website is not
    up to date and raises "credentials.run_console does not exist" error.
    Using this:
    https://stackoverflow.com/questions/75602866/google-oauth-attributeerror-installedappflow-object-has-no-attribute-run-co
    Raises error on Oauth authentication page "Request is invalid"
    '''
    return []


def get_captions_on_video(id):
    '''
    Gets the captions ids for a certain video.
    Could not get this to work. The tutorial on the Youtube API website is not
    up to date and raises "credentials.run_console does not exist" error.
    Using this:
    https://stackoverflow.com/questions/75602866/google-oauth-attributeerror-installedappflow-object-has-no-attribute-run-co
    Raises error on Oauth authentication page "Request is invalid"
    '''
    return []


def download_captions(id, file_path):
    '''
    Downloads the captions for a certain video.
    FAILING: "Expected OAuth2 access token" but i cant find where to get it.
    '''
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get("GOOGLE_API_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.captions().download(
        id = id
    )
    
    fh = io.FileIO(file_path, "wb")

    download = MediaIoBaseDownload(fh, request)
    complete = False
    while not complete:
      status, complete = download.next_chunk()


if __name__ == "__main__":
    download_captions("AUieDaarzDm-ESBmhpVrxcKZC3tSNnaAmvOIGkjauqvN_qroJWE", "requests/test.srt")