from telegram import Update
from telegram.ext import ContextTypes

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👤 Player: {user.first_name}\n"
        f"❤️ HP: 100\n"
        f"⚔️ Attack: 10\n"
        f"🛡 Defense: 5\n"
        f"💰 Gold: 50"
    )
