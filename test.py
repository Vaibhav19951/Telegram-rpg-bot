import psycopg

conn = psycopg.connect(
    "postgresql://postgres:vk@localhost:5432/rpgbot"
)

print("Connected successfully 🔥")

conn.close()
