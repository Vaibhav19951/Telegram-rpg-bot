import psycopg2

# 🔥 Neon connection string (yaha apna daal)
DATABASE_URL = "postgresql://neondb_owner:npg_Fe2PraA6zJuW@ep-shiny-dream-adn9ascd-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = True

cur = conn.cursor()


# 🔥 TABLE CREATE
def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        name TEXT,
        level INT,
        xp INT,
        gold INT,
        hp INT,
        mana INT,
        strength INT,
        vitality INT,
        agility INT,
        intelligence INT,
        sense INT,
        stat_points INT,
        inventory TEXT
    )
    """)


# 🔥 GET USER
def get_user(user_id):
    cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()

    if row:
        return {
            "user_id": row[0],
            "name": row[1],
            "level": row[2],
            "xp": row[3],
            "gold": row[4],
            "hp": row[5],
            "mana": row[6],
            "strength": row[7],
            "vitality": row[8],
            "agility": row[9],
            "intelligence": row[10],
            "sense": row[11],
            "stat_points": row[12],
            "inventory": eval(row[13]) if row[13] else []
        }
    return None


def create_user(user_id, name):
    cur.execute("""
    INSERT INTO users VALUES (
        %s, %s, 1, 0, 100, 100, 50,
        10, 10, 10, 10, 10,
        0,
        '[]'
    )
    """, (user_id, name))


# 🔥 UPDATE USER
def update_user(player):
    cur.execute("""
    UPDATE users SET
    level=%s,xp=%s,gold=%s,hp=%s,mana=%s,
    strength=%s,vitality=%s,agility=%s,
    intelligence=%s,sense=%s,stat_points=%s,
    inventory=%s
    WHERE user_id=%s
    """, (
        player["level"], player["xp"], player["gold"],
        player["hp"], player["mana"],
        player["strength"], player["vitality"], player["agility"],
        player["intelligence"], player["sense"], player["stat_points"],
        str(player["inventory"]),
        player["user_id"]
    ))
