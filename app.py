import streamlit as st
from mood_ai_advanced import MoodAI_Advanced
from playlist_generator import enrich_with_spotify

st.set_page_config(page_title="AI Mood Playlist Generator 🎶", page_icon="🎧", layout="centered")

st.title("🎶 AI Mood Playlist Generator")
st.write("🤖 Tell me about your mood, and I'll create a unique playlist for you...")

user_text = st.text_input("Describe your mood and preferred music style:")

if st.button("Generate Playlist"):
    if user_text:
        with st.spinner("Analyzing your mood and generating playlist..."):
            ai = MoodAI_Advanced()
            ai_playlist = ai.analyze_and_generate(user_text)

            st.subheader("🤖 AI Draft Playlist (keywords):")
            st.write(ai_playlist)

            spotify_playlist = enrich_with_spotify(ai_playlist, limit=15)

            st.subheader("🎧 Final Spotify Playlist:")
            for track in spotify_playlist:
                st.markdown(f"- {track}")

    else:
        st.warning("Please enter your mood and style first!")
