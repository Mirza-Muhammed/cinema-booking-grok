# recommendations.py
import openai
from booking import list_movies
import random

openai.api_key = "YOUR_OPENAI_API_KEY"

def get_recommendation():
    movies = list_movies()
    if not movies:
        return "No movies available"

    # Create a simple list of movie names
    movie_names = [m[1] for m in movies]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful cinema assistant."},
                {"role": "user", "content": f"Recommend a movie to watch from this list: {', '.join(movie_names)}"}
            ],
            temperature=0.7,
            max_tokens=50
        )
        recommendation = response.choices[0].message.content.strip()
        return recommendation
    except Exception as e:
        # fallback random recommendation
        return random.choice(movie_names)
