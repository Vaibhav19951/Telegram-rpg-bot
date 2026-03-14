
async def show_map(update, context):
    await update.message.reply_text("Mapfrom telegram import Update
from telegram.ext import ContextTypes

async def show_map(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗺 Map Locations:\n"
        "1. Village\n"
        "2. Dark Forest\n"
        "3. Dungeon Entrance"
    ) system placeholder")
