# booking.py

# Sample in-memory movie database
_movies = [
    (1, "Avatar"),
    (2, "Interstellar"),
    (3, "Inception"),
    (4, "Spider-Man: No Way Home")
]

# Each booking stored as (user_id, movie_id, seat_number)
_bookings = []

def list_movies():
    """Return all currently running movies as a list of tuples (id, name)"""
    return _movies

def book_seat(user_id, movie_id, seat_number):
    """Mock booking function"""
    _bookings.append((user_id, movie_id, seat_number))

def list_user_bookings(user_id):
    """Return all bookings for a user"""
    return [b for b in _bookings if b[0] == user_id]
