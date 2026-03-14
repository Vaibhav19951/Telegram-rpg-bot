from telegram import Update
from telegram.ext import ContextTypes

async def challenge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚔️ PvP system coming soon..."
    )
