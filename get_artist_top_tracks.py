import spotipy
import os 
from credentials import credentials

def search_artist_tracks(artist_name): 
    sp = credentials()
    results = sp.search(q='artist:' + artist_name, type='artist') 
    items = results['artists']['items']
    tracks_for_playlist = []
    # Check if artist found
    if len(items) == 0:
        print(f"Artist '{artist_name}' not found.")
        return 'No se encontro al artista'

    # Get the artist's ID
    artist_id = items[0]['id']
    # Get the artist's top tracks
    top_tracks = sp.artist_top_tracks(artist_id)
    # Print the artist's top tracks
    print(f"Top tracks of {artist_name}:")
    for track in top_tracks['tracks']:
        tracks_for_playlist.append(track)
        print(f"{track['name']} by {artist_name}")
        
    return tracks_for_playlist

if __name__ == "__main__":
   
   tracks = search_artist_tracks('Firestone')
   print(type(tracks))
   