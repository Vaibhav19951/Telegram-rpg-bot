import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN

# Import all commands
from commands.start import start
from commands.profile import profile
from commands.team import team
from commands.hunt import hunt
from commands.summon import summon
from commands.arise import arise
from commands.gates import gates
from commands.challenge import challenge
from commands.pvp import pvp
from commands.inventory import inventory
from commands.map import show_map
from commands.guild import createguild
from commands.shop import shop
from commands.dungeon import enter_dungeon
from commands.aura import aura
from commands.setaura import setaura
from commands.restart import restart

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

print("🤖 Starting RPG Bot...")

# Build bot
app = ApplicationBuilder().token(TOKEN).build()

# Register all command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("team", team))
app.add_handler(CommandHandler("hunt", hunt))
app.add_handler(CommandHandler("summon", summon))
app.add_handler(CommandHandler("arise", arise))
app.add_handler(CommandHandler("gates", gates))
app.add_handler(CommandHandler("challenge", challenge))
app.add_handler(CommandHandler("arena", pvp))
app.add_handler(CommandHandler("inventory", inventory))
app.add_handler(CommandHandler("map", show_map))
app.add_handler(CommandHandler("createguild", createguild))
app.add_handler(CommandHandler("shop", shop))
app.add_handler(CommandHandler("dungeon", enter_dungeon))
app.add_handler(CommandHandler("aura", aura))
app.add_handler(CommandHandler("setaura", setaura))
app.add_handler(CommandHandler("restart", restart))

print("✅ RPG Bot is running...")

# Start polling
app.run_polling()
