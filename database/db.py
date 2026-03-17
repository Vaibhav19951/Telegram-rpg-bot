import psycopg
from config import DATABASE_URL

# 🔥 GLOBAL CONNECTION (FAST)
conn = psycopg.connect(DATABASE_URL)
conn.autocommit = True


def get_connection():
    return conn


# 🔥 CREATE TABLES
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # USERS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        username TEXT,
        level INTEGER DEFAULT 1,
        xp INTEGER DEFAULT 0,
        gold INTEGER DEFAULT 100,
        hp INTEGER DEFAULT 100,
        strength INTEGER DEFAULT 5,
        sense INTEGER DEFAULT 0,
        aura TEXT DEFAULT '',
        stat_points INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # INVENTORY TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id SERIAL PRIMARY KEY,
        user_id BIGINT REFERENCES users(user_id) ON DELETE CASCADE,
        item_name TEXT NOT NULL,
        quantity INTEGER DEFAULT 1
    );
    """)

    cur.close()


# 🔥 GET USER
def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()

    cur.close()

    if row:
        return {
            "user_id": row[0],
            "username": row[1],
            "level": row[2],
            "xp": row[3],
            "gold": row[4],
            "hp": row[5],
            "strength": row[6],
            "sense": row[7],
            "aura": row[8],
            "stat_points": row[9]
        }

    return None


# 🔥 SAVE USER (CREATE)
def save_user(user_id, username, player):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO users (user_id, username, level, xp, gold, hp, strength, sense, aura, stat_points)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING;
    """, (
        user_id,
        username,
        player["level"],
        player["xp"],
        player["gold"],
        player["hp"],
        player["strength"],
        player["sense"],
        player["aura"],
        player["stat_points"]
    ))

    cur.close()


# 🔥 UPDATE USER
def update_user(user_id, player):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET level=%s, xp=%s, gold=%s, hp=%s, strength=%s, sense=%s, aura=%s, stat_points=%s
    WHERE user_id=%s
    """, (
        player["level"],
        player["xp"],
        player["gold"],
        player["hp"],
        player["strength"],
        player["sense"],
        player["aura"],
        player["stat_points"],
        user_id
    ))

    cur.close()
