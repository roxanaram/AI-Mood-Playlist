import os
from openai import OpenAI

class MoodAI_Advanced:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_and_generate(self, mood_text: str):
        """
        Получает от AI список жанров/артистов/ключевых слов для поиска в Spotify
        """
        prompt = f"""
        The user described their mood/music taste as: "{mood_text}".
        Generate a list of 10 search keywords (genres, moods, artists, or track names)
        that would help build a matching playlist.
        Return only the list, one keyword per line.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a music playlist assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        raw_text = response.choices[0].message.content.strip()
        keywords = [line.strip("-• ") for line in raw_text.splitlines() if line.strip()]
        return keywords
