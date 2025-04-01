import spotipy
import pprint   
from spotipy.oauth2 import SpotifyOAuth
from data import BillBoardData
import time
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIFY_ID")
client_key = os.getenv("SPOTIFY_SECRET")
redirect = "https://example.com"
scope = "playlist-modify-private,playlist-modify-public"

bbd = ""

sp_auth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_key,
    redirect_uri=redirect,
    scope=scope
)

list_uri = []
sp = spotipy.Spotify(auth_manager=sp_auth)

# ask if request a new date

ans = input("Do you wanted a new song track? y or n: ")

if ans.lower() == "y":
    bbd = BillBoardData()
    bbd.get_new_html()
else:
    bbd = BillBoardData()

track_n = int(input("How many songs do you want? 1 - 50: "))

if track_n > 50:
    track_n = 50
elif track_n < 0:   
    track_n = 50

# create a playlist
user = sp.current_user()
user_id = user['id']

res_create_playlist = sp.user_playlist_create(name=f"{bbd.date} Billboard 10", user=user_id)

playlist_id = res_create_playlist['id']

for title in bbd.data['titles'][:track_n - 1]:
    res = sp.search(title, limit=1, type="track")
    if res['tracks']['items']:
        list_uri.append(res['tracks']['items'][0]['uri'])
        print(f"Adding {title} to the list...")
    else:
        print(f"Cant find this track title {title}")
    time.sleep(2)

add_track_res = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=list_uri, position=0)
print('New playlist added, Thanks!!')
