from telegram import Update
from telegram.ext import ContextTypes
from database.db import users


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player = users.get(user_id)

    # ❌ Agar user start nahi kiya
    if not player:
        await update.message.reply_text("❌ Pehle /start kar")
        return

    # ✅ Safe data access (no crash)
    name = player.get("name", "Unknown")
    rank = player.get("rank", "E")
    level = player.get("level", 1)
    xp = player.get("xp", 0)
    gold = player.get("gold", 0)

    hp = player.get("hp", 100)
    mana = player.get("mana", 50)

    strength = player.get("strength", 10)
    vitality = player.get("vitality", 10)
    agility = player.get("agility", 10)
    intelligence = player.get("intelligence", 10)
    sense = player.get("sense", 10)

    stat_points = player.get("stat_points", 0)

    inventory = player.get("inventory", [])
    shadows = player.get("shadows", [])
    aura = player.get("aura", "None")

    # 💥 Stylish Profile Message
    msg = (
        "📜 <b>HUNTER STATUS</b>\n\n"
        f"👤 <b>Name:</b> {name}\n"
        f"🏅 <b>Rank:</b> {rank}\n"
        f"🧬 <b>Level:</b> {level}\n"
        f"✨ <b>XP:</b> {xp}\n"
        f"💰 <b>Gold:</b> {gold}\n\n"

        f"❤️ <b>HP:</b> {hp}\n"
        f"🔮 <b>Mana:</b> {mana}\n\n"

        f"⚔️ <b>Strength:</b> {strength}\n"
        f"🛡️ <b>Vitality:</b> {vitality}\n"
        f"🏃 <b>Agility:</b> {agility}\n"
        f"🧠 <b>Intelligence:</b> {intelligence}\n"
        f"👁️ <b>Sense:</b> {sense}\n\n"

        f"🎯 <b>Stat Points:</b> {stat_points}\n\n"

        f"👥 <b>Shadows:</b> {len(shadows)}\n"
        f"📦 <b>Inventory Items:</b> {len(inventory)}\n"
        f"🔥 <b>Aura:</b> {aura}"
    )

    await update.message.reply_text(msg, parse_mode="HTML")
