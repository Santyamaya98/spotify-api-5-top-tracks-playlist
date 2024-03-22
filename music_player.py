import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credentials import credentials
from get_artist_top_tracks import search_artist_tracks
import webbrowser
from time import sleep
from get_token import Get_Token
import pyautogui
import requests

def Player(artist_name):
    sp = credentials() 
    tracks = search_artist_tracks(artist_name)
    devices = sp.devices
    hrefs = [track['href'] for track in tracks]
    track, href = hrefs[:4], hrefs[4:9]
    return track, href

def songs_player(access_token, track, href):
    for i in range(len(track)):
        # Construct the request headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        # Make the request to open the track in the web browser
        response = requests.get(href[i], headers=headers)
        if response.status_code == 200:
            # Open the track in the web browser
            webbrowser.open(response.json()['external_urls']['spotify'], autoraise=True)
            # Wait for a few seconds before proceeding to the next track
            sleep(5)
        else:
            print(f"Failed to open track: {response.status_code} - {response.text}")




if __name__ == "__main__":

    token = Get_Token(client_id="ccb9ea3c2df54bb39e7bb92bd29ecb74",
    client_secret="c87f1cf33e05400186d9fb2b79d4e1b1",url = "https://accounts.spotify.com/api/token")
    print(token)
    track, href = player('feid')
    print(track, href) 
    print(type(track),type(href))
    
    
    play = songs_player(token, track, href)
    play
"""
    sp = credentials()
    result = sp.search('Ryan Castro')
    for i in range(0, len(result["tracks"]["items"])):
        new_song = result["tracks"]["items"][i]["name"]
        print(new_song)
        print(type(new_song))
"""