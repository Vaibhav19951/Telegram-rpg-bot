import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN

# Import commands
from commands.profile import profile
from commands.inventory import inventory
from commands.map import show_map
from commands.dungeon import enter_dungeon
from commands.challenge import challenge
from commands.guild import createguild
from commands.shop import shop
from commands.aura import aura
from commands.setaura import setaura


# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Start command
async def start(update, context):
    await update.message.reply_text(
        "⚔️ Welcome to the RPG Bot!\n\n"
        "Commands:\n"
        "/profile\n"
        "/inventory\n"
        "/map\n"
        "/dungeon\n"
        "/challenge\n"
        "/createguild\n"
        "/shop\n"
        "/aura\n"
        "/setaura"
    )


# Build bot
app = ApplicationBuilder().token(TOKEN).build()

# Register commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("inventory", inventory))
app.add_handler(CommandHandler("map", show_map))
app.add_handler(CommandHandler("dungeon", enter_dungeon))
app.add_handler(CommandHandler("challenge", challenge))
app.add_handler(CommandHandler("createguild", createguild))
app.add_handler(CommandHandler("shop", shop))
app.add_handler(CommandHandler("aura", aura))
app.add_handler(CommandHandler("setaura", setaura))


print("🤖 RPG Bot Running...")

app.run_polling()
