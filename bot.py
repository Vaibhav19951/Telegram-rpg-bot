from telegram.ext import ApplicationBuilder, CommandHandler

# Yahan apna Telegram Bot Token dal
TOKEN = "8128908243:AAEFTdYSF7n7KxjWbpCRUb3y3bt7oLM-_wI"

# Baaki imports aur commands
from commands.profile import profile
from commands.inventory import inventory
from commands.map import show_map
from commands.dungeon import enter_dungeon
from commands.challenge import challenge
from commands.guild import createguild
from commands.shop import shop
from commands.aura import aura

app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
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

app.run_polling()
