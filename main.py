# main.py
from chatbot import chatbot

# Simple in-memory user database
_users = {"mirza": "mirza"}  # username: password

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in _users and _users[username] == password:
        print(f"✅ Logged in as {username}")
        return username
    print("❌ Invalid credentials")
    return None

def register():
    username = input("New username: ")
    password = input("New password: ")
    if username in _users:
        print("❌ Username already exists")
        return None
    _users[username] = password
    print(f"✅ Registered as {username}")
    return username

def main():
    print("🎬 Welcome to Console Cinema Booking")
    choice = input("[1] Login  [2] Register: ")
    user_id = None
    if choice == "1":
        user_id = login()
    elif choice == "2":
        user_id = register()
    if not user_id:
        return
    chatbot(user_id)

if __name__ == "__main__":
    main()
