from telegram import Update
from telegram.ext import ContextTypes

async def inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎒 Inventory:\n"
        "- Wooden Sword\n"
        "- 2 Health Potions\n"
        "- Old Shield"
    )
