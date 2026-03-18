from telegram import Update
from telegram.ext import ContextTypes
from database.db import users


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id in users:
        await update.message.reply_text("✅ Tu already start kar chuka hai")
        return

    users[user_id] = {
        "name": update.effective_user.first_name,
        "rank": "E",
        "level": 1,
        "xp": 0,
        "gold": 100,

        "hp": 100,
        "mana": 50,

        "strength": 10,
        "vitality": 10,
        "agility": 10,
        "intelligence": 10,
        "sense": 10,

        "stat_points": 0,

        "inventory": [],
        "shadows": [],
        "aura": "None",
        "last_boss": None
    }

    await update.message.reply_text("🔥 Game start ho gaya!\n\nAb /profile try kar")
