# Mood-Based Playlist Generator

![Python](https://img.shields.io/badge/Language-Python_3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![OpenAI](https://img.shields.io/badge/AI-OpenAI_GPT--4o--mini-412991?logo=openai)
![Spotify](https://img.shields.io/badge/API-Spotify-1DB954?logo=spotify)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A web application that creates personalized Spotify playlists by analyzing your emotional state using AI and matching it with appropriate music.

## How It Works

You describe your current mood or emotional state in natural language, and the application:

1. **Analyzes your input** using OpenAI's GPT-4o-mini to identify the underlying emotion and music preferences
2. **Generates a playlist** of 10 songs tailored to that mood
3. **Retrieves Spotify links** for each track using the Spotify Web API

The entire process runs through a Streamlit interface, requiring no Spotify login (uses Client Credentials flow).

## Technical Architecture

**Core Technologies:**
- **Streamlit** - Web interface
- **OpenAI GPT-4o-mini** - Mood interpretation and music recommendation
- **Spotify Web API** - Track metadata and links
- **Python 3.10+** - Backend logic

**API Integration:**
- OpenAI API for natural language understanding
- Spotify Client Credentials flow for track search (read-only access)

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/roxanaram/AI-Mood-Playlist.git
cd AI-Mood-Playlist
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages: `streamlit`, `openai`, `spotipy`, `python-dotenv`, `requests`

### 3. Configure API Keys

Create a `.env` file in the project root (this file is gitignored):
```ini
OPENAI_API_KEY=sk-...
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

**Getting API credentials:**
- **OpenAI:** Create an API key at https://platform.openai.com/api-keys
- **Spotify:** Register an application at https://developer.spotify.com/dashboard

### 4. Launch the Application
```bash
streamlit run app.py
```

Access the app at `http://localhost:8501` in your browser.

## Usage Example

**Input:** "I'm feeling nostalgic and want something mellow"

**Output:** 
- AI identifies the mood as nostalgic/reflective
- Generates 10 song recommendations (e.g., indie folk, acoustic)
- Provides clickable Spotify links for each track

## Code Structure
```
AI_Mood_Playlist_Generator_v4/
├── app.py                    # Streamlit UI and main application flow
├── main.py                   # Optional CLI entry point
├── mood_ai_advanced.py       # GPT integration for mood detection
├── playlist_generator.py     # Spotify API interaction and track selection
├── utils.py                  # Helper functions
├── requirements.txt          # Python dependencies
├── .env.example              # Template for API configuration
└── README.md
```

**Module descriptions:**
- `mood_ai_advanced.py` - Constructs prompts for GPT and parses emotional analysis
- `playlist_generator.py` - Queries Spotify API based on mood parameters
- `app.py` - Handles user input, coordinates modules, displays results

## Limitations and Future Work

**Current limitations:**
- Client Credentials flow limits access to public Spotify data (no user playlist creation)
- Playlist is generated fresh each time (no persistence)
- Limited to 10 tracks per generation

**Potential improvements:**
- Add Spotify OAuth to save playlists directly to user accounts
- Implement playlist caching to avoid redundant API calls
- Support for playlist length customization
- Multi-mood blending (e.g., "energetic but melancholic")

## License

MIT License - feel free to fork and modify.
