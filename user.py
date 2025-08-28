import bcrypt
from database import get_connection

def register(username, password):
    conn = get_connection()
    c = conn.cursor()
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, pw_hash))
        conn.commit()
        print("✅ Registration successful!")
    except:
        print("⚠ Username already exists!")
    conn.close()

def login(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row and bcrypt.checkpw(password.encode(), row[1]):
        return row[0]  # return user_id
    return None
