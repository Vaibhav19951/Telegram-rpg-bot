import random
import os
from telegram import Update
from telegram.ext import ContextTypes
from database.db import users
from data.monsters import MONSTERS


def get_required_xp(level: int) -> int:
    if level >= 30:
        return 30000
    return level * level * 100


def xp_bar(current, total, length=10):
    if total == 0:
        return "░" * length
    filled = int(length * current / total)
    return "█" * filled + "░" * (length - filled)


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


# 🔥 AUTO IMAGE MATCH (NO EDIT NEEDED)
def find_image(monster_name):
    if not os.path.exists("images"):
        return None

    files = os.listdir("images")

    # normalize name
    clean_name = monster_name.lower().replace(" ", "")

    for file in files:
        file_name = file.lower().replace("_", "").replace(" ", "").replace(".png", "").replace(".jpg", "")

        if clean_name in file_name:
            return os.path.join("images", file)

    return os.path.join("images", "default.png")


async def hunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player = users.get(user_id)

    if not player:
        await update.message.reply_text(
            "❌ <b>You need to start first!</b>\nUse /start",
            parse_mode="HTML"
        )
        return

    monster = get_monster_by_level(player["level"])

    name = monster["name"]
    rank = monster["rank"]

    gold = monster.get("gold", random.randint(20, 80))
    xp = monster.get("xp", random.randint(10, 30))

    player["gold"] += gold
    player["xp"] += xp
    player["last_boss"] = name

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

    bar = xp_bar(player["xp"], required_xp)

    caption = (
        "⚔️ <b>HUNT RESULT</b> ⚔️\n\n"
        f"👹 <b>Monster:</b> {name}\n"
        f"🏅 <b>Rank:</b> {rank}\n\n"

        f"💰 Gold: {gold}\n"
        f"✨ XP: {xp}\n\n"

        f"🧬 Level: {player['level']}\n"
        f"📊 XP: {player['xp']}/{required_xp}\n"
        f"{bar}\n\n"

        f"🎯 Stat Points: {player['stat_points']}"
        f"{level_up_msg}"
    )

    image_path = find_image(name)

    try:
        if image_path and os.path.exists(image_path):
            with open(image_path, "rb") as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=caption,
                    parse_mode="HTML"
                )
        else:
            await update.message.reply_text(caption, parse_mode="HTML")

    except Exception as e:
        print("Image error:", e)
        await update.message.reply_text(caption, parse_mode="HTML")
