# seat_availability.py
from booking import _bookings

TOTAL_SEATS = 20

def tool_check_seat(movie_id):
    booked = len([b for b in _bookings if b[1] == movie_id])
    available = TOTAL_SEATS - booked
    return f"Seats available: {available}"
