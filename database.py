import sqlite3

def init_db():
    conn = sqlite3.connect("subscriptions.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            plan TEXT,
            expires_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def set_subscription(user_id, plan, expires_at):
    conn = sqlite3.connect("subscriptions.db")
    c = conn.cursor()
    c.execute("REPLACE INTO users (user_id, plan, expires_at) VALUES (?, ?, ?)",
              (user_id, plan, expires_at))
    conn.commit()
    conn.close()

def get_subscription(user_id):
    conn = sqlite3.connect("subscriptions.db")
    c = conn.cursor()
    c.execute("SELECT plan, expires_at FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result
