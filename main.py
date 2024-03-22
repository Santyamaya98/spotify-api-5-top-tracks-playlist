#"@sac98"

from music_player import Player, songs_player
from get_token import Get_Token

def main(name_artist):


    track, href = Player(name_artist)
    player = songs_player(token, track, href) 

    return player


if __name__ == "__main__":
    token = Get_Token(client_id="ccb9ea3c2df54bb39e7bb92bd29ecb74",
    client_secret="c87f1cf33e05400186d9fb2b79d4e1b1",url = "https://accounts.spotify.com/api/token")
    name_artist = input('ingresa el nombre del artissta tal como aparece en spotify')   
    player = main(name_artist)
    player