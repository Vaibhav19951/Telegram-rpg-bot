import psycopg
from config import DATABASE_URL


# 🔌 CONNECTION
def get_connection():
    return psycopg.connect(DATABASE_URL)


# 🏗 CREATE TABLES
def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:

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

            # HUNT STATS
            cur.execute("""
            CREATE TABLE IF NOT EXISTS hunt_stats (
                user_id BIGINT PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
                total_hunts INTEGER DEFAULT 0,
                bosses_killed INTEGER DEFAULT 0
            );
            """)


# 👤 LOAD USER
def get_user(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            row = cur.fetchone()

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


# 💾 SAVE USER
def save_user(user_id, username, player):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO users (user_id, username, level, xp, gold, hp, strength, sense, aura, stat_points)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (user_id) DO UPDATE SET
                username = EXCLUDED.username,
                level = EXCLUDED.level,
                xp = EXCLUDED.xp,
                gold = EXCLUDED.gold,
                hp = EXCLUDED.hp,
                strength = EXCLUDED.strength,
                sense = EXCLUDED.sense,
                aura = EXCLUDED.aura,
                stat_points = EXCLUDED.stat_points
            """, (
                user_id,
                username,
                player["level"],
                player["xp"],
                player["gold"],
                player["hp"],
                player["strength"],
                player.get("sense", 0),
                player.get("aura", ""),
                player.get("stat_points", 0)
            ))


# 🎒 ADD ITEM
def add_item(user_id, item_name, quantity=1):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO inventory (user_id, item_name, quantity)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id, item_name)
            DO UPDATE SET quantity = inventory.quantity + %s
            """, (user_id, item_name, quantity, quantity))


# 🎒 GET INVENTORY
def get_inventory(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT item_name, quantity FROM inventory
            WHERE user_id = %s
            """, (user_id,))
            return cur.fetchall()
