import random
from telegram import Update
from telegram.ext import ContextTypes
from database.db import users
from data.monsters import MONSTERS


def get_required_xp(level: int) -> int:
    if level >= 30:
        return 30000
    return level * level * 100


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


async def hunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player = users.get(user_id)

    if not player:
        await update.message.reply_text(
            "❌ <b>You need to start first!</b>\nUse /start",
            parse_mode="HTML"
        )
        return

    # 🎯 Monster select
    monster = get_monster_by_level(player["level"])

    name = monster["name"]
    rank = monster["rank"]
    image = monster["image"]  # ⚠️ ye MONSTERS me hona chahiye

    # 💰 Rewards
    gold = random.randint(30, 100)
    xp = random.randint(20, 50)

    player["gold"] += gold
    player["xp"] += xp
    player["last_boss"] = name

    # 🔥 LEVEL UP SYSTEM
    required_xp = get_required_xp(player["level"])

    level_up_msg = ""
    if player["xp"] >= required_xp:
        player["xp"] -= required_xp
        player["level"] += 1
        player["stat_points"] += 5

        level_up_msg = (
            "\n\n🔥 <b>LEVEL UP!</b> 🔥\n"
            f"🧬 New Level: {player['level']}\n"
            f"🎯 +5 Stat Points"
        )

    # 💥 STYLISH MESSAGE
    caption = (
        "⚔️ <b>HUNT RESULT</b> ⚔️\n\n"
        f"👹 <b>Monster:</b> {name}\n"
        f"🏅 <b>Rank:</b> {rank}\n\n"
        f"💰 <b>Gold Earned:</b> {gold}\n"
        f"✨ <b>XP Gained:</b> {xp}\n\n"
        f"🧬 <b>Level:</b> {player['level']}\n"
        f"📊 <b>XP:</b> {player['xp']}/{required_xp}"
        f"{level_up_msg}"
    )

    # 📸 IMAGE + TEXT SAME MESSAGE
    await update.message.reply_photo(
        photo=image,
        caption=caption,
        parse_mode="HTML"
    )
