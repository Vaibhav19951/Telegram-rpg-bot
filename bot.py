
import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from commands.profile import profile
from commands.inventory import inventory
from commands.map import show_map
from commands.dungeon import enter_dungeon
from commands.challenge import challenge
from commands.guild import createguild, joinguild
from commands.aura import aura
from commands.shop import shop

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("inventory", inventory))
    app.add_handler(CommandHandler("map", show_map))
    app.add_handler(CommandHandler("dungeon", enter_dungeon))
    app.add_handler(CommandHandler("challenge", challenge))
    app.add_handler(CommandHandler("createguild", createguild))
    app.add_handler(CommandHandler("joinguild", joinguild))
    app.add_handler(CommandHandler("aura", aura))
    app.add_handler(CommandHandler("shop", shop))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
