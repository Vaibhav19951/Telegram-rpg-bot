import psycopg
from config import DATABASE_URL

def get_connection():
    return psycopg.connect(DATABASE_URL)

def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id BIGINT PRIMARY KEY,
                    username TEXT,
                    level INTEGER DEFAULT 1,
                    xp INTEGER DEFAULT 0,
                    gold INTEGER DEFAULT 100,
                    hp INTEGER DEFAULT 100,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT REFERENCES users(user_id) ON DELETE CASCADE,
                    item_name TEXT NOT NULL,
                    quantity INTEGER DEFAULT 1
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS hunt_stats (
                    user_id BIGINT PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
                    total_hunts INTEGER DEFAULT 0,
                    total_kills INTEGER DEFAULT 0,
                    bosses_killed INTEGER DEFAULT 0
                );
            """)
        conn.commit()

def register_user(user_id: int, username: str | None):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (user_id, username)
                VALUES (%s, %s)
                ON CONFLICT (user_id) DO NOTHING;
            """, (user_id, username))

            cur.execute("""
                INSERT INTO hunt_stats (user_id)
                VALUES (%s)
                ON CONFLICT (user_id) DO NOTHING;
            """, (user_id,))
        conn.commit()

def get_user(user_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT user_id, username, level, xp, gold, hp
                FROM users
                WHERE user_id = %s;
            """, (user_id,))
            return cur.fetchone()

def add_gold(user_id: int, amount: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE users
                SET gold = gold + %s
                WHERE user_id = %s;
            """, (amount, user_id))
        conn.commit()

def add_item(user_id: int, item_name: str, quantity: int = 1):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT quantity FROM inventory
                WHERE user_id = %s AND item_name = %s;
            """, (user_id, item_name))
            row = cur.fetchone()

            if row:
                cur.execute("""
                    UPDATE inventory
                    SET quantity = quantity + %s
                    WHERE user_id = %s AND item_name = %s;
                """, (quantity, user_id, item_name))
            else:
                cur.execute("""
                    INSERT INTO inventory (user_id, item_name, quantity)
                    VALUES (%s, %s, %s);
                """, (user_id, item_name, quantity))
        conn.commit()

def get_inventory(user_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT item_name, quantity
                FROM inventory
                WHERE user_id = %s
                ORDER BY item_name ASC;
            """, (user_id,))
            return cur.fetchall()
