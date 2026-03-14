
import sqlite3

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS players(
id INTEGER PRIMARY KEY,
level INTEGER,
coins INTEGER,
class TEXT,
aura TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS guilds(
name TEXT,
leader INTEGER
)
''')

conn.commit()
