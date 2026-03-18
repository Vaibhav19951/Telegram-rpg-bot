import random
import os
from telegram import Update
from telegram.ext import ContextTypes
from database.db import users
from data.monsters import MONSTERS


# 🔥 XP requirement
def get_required_xp(level: int) -> int:
    if level >= 30:
        return 30000
    return level * level * 100


# 🔥 XP bar
def xp_bar(current, total, length=10):
    if total == 0:
        return "░" * length
    filled = int(length * current / total)
    return "█" * filled + "░" * (length - filled)


# 🔥 monster select
def get_monster_by_level(player_level):
    if player_level <= 5:
        pool = [m for m in MONSTERS if m["rank"] == "E"]
    elif player_level <= 10:
        pool = [m for m in MONSTERS if m["rank"] in ["E", "D"]]
    elif player_level <= 15:
        pool = [m for m in MONSTERS if m["rank"] in ["D", "C"]]
    elif player_level <= 20:
        pool = [m for m in MONSTERS if m["rank"] in ["C", "B"]]
    else:
        pool = [m for m in MONSTERS if m["rank"] in ["B", "A"]]

    return random.choice(pool)


# 🔥 auto image path
def get_image_path(monster_name):
    filename = monster_name.lower().replace(" ", "_") + ".png"
    return f"images/{filename}"


# 🔥 MAIN COMMAND
async def hunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player = users.get(user_id)

    # ❌ user not started
    if not player:
        await update.message.reply_text(
            "❌ <b>You need to start first!</b>\nUse /start",
            parse_mode="HTML"
        )
        return

    # 🎯 monster
    monster = get_monster_by_level(player["level"])
    name = monster["name"]
    rank = monster["rank"]

    # 💰 rewards
    gold = monster.get("gold", random.randint(20, 80))
    xp = monster.get("xp", random.randint(10, 30))

    player["gold"] += gold
    player["xp"] += xp
    player["last_boss"] = name

    # 🔥 level up
    required_xp = get_required_xp(player["level"])
    level_up_msg = ""

    if player["xp"] >= required_xp:
        player["xp"] -= required_xp
        player["level"] += 1
        player["stat_points"] += 5

        level_up_msg = (
            "\n\n🔥 <b>LEVEL UP!</b>\n"
            f"🧬 Level: {player['level']}\n"
            f"🎯 +5 Stat Points"
        )

    # 📊 xp bar
    bar = xp_bar(player["xp"], required_xp)

    # 💥 FULL STYLISH MESSAGE
    caption = (
        "╔═══ ⚔️ <b>HUNT RESULT</b> ⚔️ ═══╗\n\n"

        f"👹 <b>Monster:</b> {name}\n"
        f"🏅 <b>Rank:</b> {rank}\n\n"

        "───────────────\n\n"

        f"💰 <b>Gold:</b> {gold}\n"
        f"✨ <b>XP:</b> {xp}\n\n"

        "───────────────\n\n"

        f"🧬 <b>Level:</b> {player['level']}\n"
        f"📊 <b>XP:</b> {player['xp']}/{required_xp}\n"
        f"{bar}\n\n"

        f"❤️ <b>HP:</b> {player.get('hp', 100)}\n"
        f"🔮 <b>Mana:</b> {player.get('mana', 50)}\n\n"

        "───────────────\n\n"

        f"⚔️ STR: {player.get('strength', 10)}\n"
        f"🛡️ VIT: {player.get('vitality', 10)}\n"
        f"🏃 AGI: {player.get('agility', 10)}\n"
        f"🧠 INT: {player.get('intelligence', 10)}\n"
        f"👁️ SEN: {player.get('sense', 10)}\n\n"

        "───────────────\n\n"

        f"🎯 <b>Stat Points:</b> {player['stat_points']}"
        f"{level_up_msg}\n\n"

        "╚════════════════════╝"
    )

    # 📸 IMAGE SEND
    image_path = get_image_path(name)

    try:
        if not os.path.exists(image_path):
            image_path = "images/default.png"

        with open(image_path, "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=caption,
                parse_mode="HTML"
            )

    except Exception as e:
        print("Image error:", e)
        await update.message.reply_text(caption, parse_mode="HTML")
