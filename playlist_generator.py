import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

def enrich_with_spotify(ai_songs, limit=10):
    final_playlist = []
    for song in ai_songs:
        results = sp.search(q=song, type='track', limit=1)
        tracks = results.get("tracks", {}).get("items", [])
        if tracks:
            track = tracks[0]
            final_playlist.append(f"{track['name']} - {track['artists'][0]['name']}")
        if len(final_playlist) >= limit:
            break

    return final_playlist
