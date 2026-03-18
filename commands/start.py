from telegram import Update
from telegram.ext import ContextTypes
from database.db import get_user, create_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    name = user.first_name

    # 🔍 check existing user
    player = get_user(user_id)

    if player:
        await update.message.reply_text(
            "⚡ <b>You are already a Hunter!</b>",
            parse_mode="HTML"
        )
        return

    # 🔥 CREATE USER WITH FULL DATA
    create_user(user_id, name)

    await update.message.reply_text(
        "🔥 <b>WELCOME, HUNTER!</b> 🔥\n\n"
        "⚔️ Your journey has begun...\n\n"
        "🧬 Rank: E\n"
        "🎒 Inventory: Empty\n\n"
        "💡 Use /hunt to start fighting monsters!",
        parse_mode="HTML"
    )
