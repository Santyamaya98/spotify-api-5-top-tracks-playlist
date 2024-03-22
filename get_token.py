
import os
import requests 
import json 
from dotenv import load_dotenv


def Get_Token(client_id, client_secret, url):
    auth_string = client_id + ":" + client_secret 
    headers = {
        
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    # Set the data for the POST request
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
        } 
    # Send the POST request to obtain the access token
    response = requests.post(url, headers=headers, data=data)

    # Parse the response as JSON
    response_data = response.json()
    token = response_data["access_token"]
    # Print the response
    return token 
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_track(token, track):
    url = "https://api.spotify.com/v1/me/shows?offset=0&limit=20"
    headers = get_auth_header(token)
    query = f"q={track}&type=track&limit=1"
    query_url = url + query
    response = requests.get(query_url,headers=headers)
    return response 
if __name__ == "__main__":
    
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    url = "https://accounts.spotify.com/api/token"

    token = Get_Token(client_id, client_secret, url)
    print(token)
    print(get_auth_header(token))
    searched_track = input('que deseas buscar  ')
    track_selected = search_track(token, search_track)
    print(track_selected)

