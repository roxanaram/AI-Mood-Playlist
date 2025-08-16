from mood_ai_advanced import MoodAI_Advanced
from playlist_generator import enrich_with_spotify
from utils import print_welcome, display_playlist

def main():
    print_welcome()
    user_text = input("Describe your mood and preferred music style: ")

    ai = MoodAI_Advanced()
    ai_playlist = ai.analyze_and_generate(user_text)

    print("\n🤖 AI Draft Playlist (raw):")
    for s in ai_playlist[:10]:
        print("-", s)

    print("\n🔎 Searching Spotify for real matches...")
    spotify_playlist = enrich_with_spotify(ai_playlist, limit=15)

    display_playlist(spotify_playlist)

if __name__ == "__main__":
    main()
