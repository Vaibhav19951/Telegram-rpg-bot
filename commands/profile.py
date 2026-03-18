from telegram import Update
from telegram.ext import ContextTypes
from database.db import users


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player = users.get(user_id)

    if not player:
        await update.message.reply_text(
            "❌ <b>You need to start first!</b>\n\nUse /start",
            parse_mode="HTML"
        )
        return

    msg = (
        "📜 <b>HUNTER STATUS</b> 📜\n\n"

        f"👤 <b>Name:</b> {player.get('name')}\n"
        f"🏅 <b>Rank:</b> {player.get('rank')}\n"
        f"🧬 <b>Level:</b> {player.get('level')}\n"
        f"✨ <b>XP:</b> {player.get('xp')}\n"
        f"💰 <b>Gold:</b> {player.get('gold')}\n\n"

        f"❤️ <b>HP:</b> {player.get('hp')}\n"
        f"🔮 <b>Mana:</b> {player.get('mana')}\n\n"

        f"⚔️ <b>Strength:</b> {player.get('strength')}\n"
        f"🛡️ <b>Vitality:</b> {player.get('vitality')}\n"
        f"🏃 <b>Agility:</b> {player.get('agility')}\n"
        f"🧠 <b>Intelligence:</b> {player.get('intelligence')}\n"
        f"👁️ <b>Sense:</b> {player.get('sense')}\n\n"

        f"🎯 <b>Stat Points:</b> {player.get('stat_points')}\n\n"

        f"👥 <b>Shadows:</b> {len(player.get('shadows', []))}\n"
        f"📦 <b>Inventory Items:</b> {len(player.get('inventory', []))}\n"
        f"🔥 <b>Aura:</b> {player.get('aura')}"
    )

    await update.message.reply_text(msg, parse_mode="HTML")
