from telegram import Update
from telegram.ext import ContextTypes
from database.db import users


async def inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player = users.get(user_id)

    if not player:
        await update.message.reply_text("❌ Use /start first")
        return

    inv = player.get("inventory", [])

    if not inv:
        items_text = "Empty"
    else:
        items_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(inv)])

    msg = (
        f"🎒 <b>{player['name']}'s Inventory</b>\n\n"
        f"{items_text}\n\n"
        f"💰 Gold: {player['gold']}\n"
        f"❤️ HP: {player['hp']}\n"
        f"⚔️ Attack: {player['strength']}\n"
        f"🛡️ Defense: {player['vitality']}"
    )

    await update.message.reply_text(msg, parse_mode="HTML")
