# AI Mood-Based Playlist Generator v4

🎧 An interactive Streamlit web app that generates personalized Spotify playlists based on your mood using GPT and the Spotify API.

## Features
- **AI-powered mood detection** (GPT-4o-mini)
- **Smart playlist generation** (10 songs) based on emotion and genre
- **Spotify API integration** (Client Credentials flow, no login required)
- **Lightweight & easy to run**

## Setup
1. Clone this repo
```bash
git clone https://github.com/your-username/ai-mood-playlist.git
cd ai-mood-playlist
```
2. Create `.env` from `.env.example` and add your API keys
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app in Terminal:
```bash
streamlit run app.py
```

✅ No Spotify login required — just run and enjoy your AI DJ!

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