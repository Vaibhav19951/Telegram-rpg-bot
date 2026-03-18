from telegram import Update
from telegram.ext import ContextTypes
from database.db import users, save_data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    # 🧠 already exists check
    if user_id in users:
        await update.message.reply_text(
            "⚡ <b>You are already a Hunter!</b>",
            parse_mode="HTML"
        )
        return

    # 🔥 create new player
    users[user_id] = {
        "name": user.first_name,
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

        "inventory": [],   # 🎒 IMPORTANT
        "shadows": [],
        "aura": "None",

        "last_boss": None
    }

    # 💾 SAVE DATA
    save_data()

    # 💥 stylish welcome
    msg = (
        "🔥 <b>WELCOME, HUNTER!</b> 🔥\n\n"
        "⚔️ Your journey has begun...\n\n"
        "🧬 Rank: E\n"
        "stats : 0"
        "💡 Use /hunt to start fighting monsters!"
    )

    await update.message.reply_text(msg, parse_mode="HTML")
