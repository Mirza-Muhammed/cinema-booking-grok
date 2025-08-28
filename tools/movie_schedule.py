# movie_schedule.py
from booking import list_movies

def tool_get_schedule():
    """
    Returns a nicely formatted string of all current movies and showtimes.
    """
    movies = list_movies()
    if not movies:
        return "No movies currently running."

    output = "🎬 Movie Schedule:\n"
    for movie in movies:
        movie_id, name = movie
        output += f"{movie_id}. {name} at 6:00 PM (20 seats left)\n"
    return output
