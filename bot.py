import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN

# Commands
from commands.profile import profile
from commands.inventory import inventory
from commands.map import show_map
from commands.dungeon import enter_dungeon
from commands.challenge import challenge
from commands.guild import createguild
from commands.shop import shop
from commands.aura import aura

# Database
from database.db import load_players, save_players

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load player data
players = load_players()

# Build bot application
app = ApplicationBuilder().token(TOKEN).build()

# Register command handlers
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("inventory", inventory))
app.add_handler(CommandHandler("map", show_map))
app.add_handler(CommandHandler("dungeon", enter_dungeon))
app.add_handler(CommandHandler("challenge", challenge))
app.add_handler(CommandHandler("createguild", createguild))
app.add_handler(CommandHandler("shop", shop))
app.add_handler(CommandHandler("aura", aura))
app.add_handler(CommandHandler("setaura", aura))

print("🔥 RPG BOT RUNNING...")

try:
    app.run_polling()
finally:
    save_players(players)
