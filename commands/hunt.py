import random
import os
from telegram import Update
from telegram.ext import ContextTypes
from database.db import users
from data.monsters import MONSTERS
from systems.combat import fight
from systems.rewards import give_rewards
from database.db import save_data


# 🔥 XP requirement
def get_required_xp(level: int) -> int:
    return level * level * 100


# 🔥 XP bar
def xp_bar(current, total, length=10):
    if total == 0:
        return "░" * length
    filled = int(length * current / total)
    return "█" * filled + "░" * (length - filled)


# 🔥 monster select
def get_monster_by_level(player_level):
    pool = [m for m in MONSTERS if m.get("rank") == "E"]
    return random.choice(pool)


# 🔥 auto image match
def find_image(monster_name):
    try:
        if not os.path.exists("images"):
            return None

        files = os.listdir("images")
        clean_name = monster_name.lower().replace(" ", "")

        for file in files:
            file_name = file.lower().replace("_", "").replace(".png", "").replace(".jpg", "")
            if clean_name in file_name:
                return os.path.join("images", file)

        return "images/default.png"

    except:
        return None


# ⚔️ MAIN COMMAND
async def hunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        player = users.get(user_id)

        if not player:
            await update.message.reply_text("❌ Use /start first")
            return

        # 🎯 get monster
        monster = get_monster_by_level(player["level"])

        # ⚔️ fight
        win, log = fight(player, monster)
        battle_log = "\n".join(log)

        # 🎁 rewards
        if win:
            rewards = give_rewards(player, monster)
        else:
            rewards = {}

        # 📊 xp bar
        required_xp = get_required_xp(player["level"])
        bar = xp_bar(player["xp"], required_xp)

        # 🎁 reward text
        reward_text = ""
        if "gold" in rewards:
            reward_text += f"💰 Gold: {rewards['gold']}\n"
        if "xp" in rewards:
            reward_text += f"✨ XP: {rewards['xp']}\n"
        if "item" in rewards:
            reward_text += f"🎒 Item: {rewards['item']}\n"

        # 💥 FINAL MESSAGE
        caption = (
            "⚔️ <b>BATTLE RESULT</b> ⚔️\n\n"
            f"{battle_log}\n\n"
            f"📊 XP: {player['xp']}/{required_xp}\n"
            f"{bar}\n\n"
            f"🎁 <b>Rewards</b>\n{reward_text}"
        )

        # 📸 image send
        image_path = find_image(monster["name"])

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
        print("💀 HUNT ERROR:", e)
        await update.message.reply_text("❌ Error in hunt system")
