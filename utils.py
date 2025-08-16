def print_welcome():
    print("🎶 Welcome to AI Mood Playlist Generator v4!")
    print("🤖 Tell me about your mood, and I'll create a unique playlist for you...\n")

def display_playlist(playlist):
    print("\n🎧 Your AI-curated playlist:")
    for i, song in enumerate(playlist, 1):
        print(f"{i}. {song}")
