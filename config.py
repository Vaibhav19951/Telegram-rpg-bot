TOKEN = "7990370974:AAFBBOIOneO3cbN4RVWlfGrgWuLkGT5gZsY"

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "rpgbot"
DB_USER = "postgres"
DB_PASSWORD = "your_password"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
