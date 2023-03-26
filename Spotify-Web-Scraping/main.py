import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = ""
CLIENT_SECRET = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

data = input("Para qual ano você deseja viajar? Escreva a data no formato YYYY-MM-DD: ")
year = data.split("-")[0]

URL_DIA = f"https://www.billboard.com/charts/hot-100/{data}"

response = requests.get(URL_DIA)

soup = BeautifulSoup(response.text, "html.parser")
songs_name = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-"
                                        "size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@"
                                        "mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
list_songs = [name.getText() for name in songs_name]
new_list = []
song_uris = []
for song in list_songs:
    songs = song.replace("\n", "")
    songs = songs.replace("\t", "")
    result = sp.search(q=f"track:{songs} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{songs} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user_id, f"Playlist - {data}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
