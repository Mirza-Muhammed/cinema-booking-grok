# chatbot.py
import openai
import json
from booking import list_movies, book_seat
from tools import seat_availability, movie_schedule, mock_payment
from recommendations import get_recommendation
import re

openai.api_key = "YOUR_OPENAI_API_KEY"

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def parse_intent(user_input, movie_names):
    keywords = {
        "schedule": "check_schedule",
        "movies": "check_schedule",
        "show": "check_schedule",
        "seat": "check_seat",
        "seats": "check_seat",
        "book": "book_ticket",
        "booking": "book_ticket",
        "recommend": "recommend",
        "suggest": "recommend",
    }

    for k, v in keywords.items():
        if k in user_input.lower():
            action = v
            break
    else:
        action = None

    prompt = f"""
    You are a friendly cinema booking assistant. 
    User input: "{user_input}".
    Determine the user's intent: "check_schedule", "check_seat", "book_ticket", "recommend", or "chat".
    If a movie is mentioned, return "movie_name" as typed.
    Available movies (normalized): {list(movie_names.keys())}.
    Return JSON only: {{"action": intent, "movie_name": name if mentioned}}
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0
        )
        data = json.loads(response.choices[0].text.strip())
        if "movie_name" in data:
            normalized = normalize(data["movie_name"])
            if normalized in movie_names:
                data["movie_id"] = movie_names[normalized]
        if action and data.get("action") in [None, "chat"]:
            data["action"] = action
        return data
    except:
        return {"action": action or "chat"}

def chatbot(user_id):
    movies_dict = {normalize(m[1]): m[0] for m in list_movies()}

    print("\n💬 Chatbot ready! Ask naturally about movies, seats, bookings, or recommendations.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        intent = parse_intent(user_input, movies_dict)
        action = intent.get("action")
        movie_id = intent.get("movie_id")
        movie_name = intent.get("movie_name")

        if action == "check_schedule":
            print(movie_schedule.tool_get_schedule())

        elif action == "check_seat":
            if not movie_id:
                movie_name_input = input("Which movie are you asking about? ").lower()
                movie_id = movies_dict.get(normalize(movie_name_input))
                if not movie_id:
                    print("❌ Movie not found.")
                    continue
            print(seat_availability.tool_check_seat(movie_id))

        elif action == "book_ticket":
            if not movie_id:
                movie_name_input = input("Which movie would you like to book? ").lower()
                movie_id = movies_dict.get(normalize(movie_name_input))
                if not movie_id:
                    print("❌ Movie not found.")
                    continue
            try:
                seat_number = int(input("Enter seat number to book: "))
            except ValueError:
                print("❌ Invalid seat number.")
                continue
            mock_payment.tool_mock_payment(10)
            book_seat(user_id, movie_id, seat_number)
            print("✅ Booking confirmed!")

        elif action == "recommend":
            print("🎯 Recommendation:", get_recommendation())

        elif action == "chat":
            print("🤖 Hi! I can help you check movies, seats, book tickets, or give recommendations. 😊")

        else:
            print("🤖 Sorry, I couldn't understand that. Try asking about movies, seats, booking, or recommendations.")
