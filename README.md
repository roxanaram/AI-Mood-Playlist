# AI Mood-Based Playlist Generator v4

🎧 An interactive Streamlit web app that generates personalized Spotify playlists based on your mood using GPT and the Spotify API.

## Features
- **AI-powered mood detection** (GPT-4o-mini)
- **Smart playlist generation** (10 songs) based on emotion and genre
- **Spotify API integration** (Client Credentials flow, no login required)
- **Lightweight & easy to run**

## Installation
1. Clone this repository and install dependencies:
```bash
git clone https://github.com/roxanaram/AI-Mood-Playlist.git
cd AI-Mood-Playlist
pip install -r requirements.txt
```

1. Create a `.env` file in the project root:
```ini
OPENAI_API_KEY=your_openai_api_key_here
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```
**⚠️ Never commit .env to GitHub! (It’s already ignored in .gitignore.)**

2. Replace `your_openai_api_key_here` and Spotify credentials with your own.

## Run the App
```bash
streamlit run app.py
```
Then open the provided localhost URL in your browser.


## Example Usage

- Enter your mood (e.g., nostalgic, happy, energetic)
- AI suggests a playlist based on emotion & music preferences 
- Spotify links generated automatically 🎶

## Technologies Used

- Streamlit 
- Python 3.10+ 
- OpenAI GPT (for mood analysis)
- Spotify Web API 
- dotenv, requests

## Project Structure
```graphhql
AI_Mood_Playlist_Generator_v4/
│── app.py                  # Streamlit app (UI)
│── main.py                 # CLI entry point (optional)
│── mood_ai_advanced.py     # AI mood detection
│── playlist_generator.py   # Playlist creation logic
│── utils.py                # Helper functions
│── requirements.txt        # Dependencies
│── .env.example            # API keys template

```
