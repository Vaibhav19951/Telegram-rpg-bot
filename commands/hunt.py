import random
from data.monsters import MONSTERS
from database.db import users


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


async def hunt(update, context):
    user = update.effective_user

    player = get_user(user.id)

    if not player:
        await update.message.reply_text("⚠️ First use /start")
        return

    # 👾 MONSTER PICK
    monster = get_monster_by_level(player["level"])

    # ⚔ DAMAGE
    damage = player["strength"] * 5
    monster_hp_left = monster["hp"] - damage

    # 🎁 REWARDS
    player["xp"] += monster["xp"]
    player["gold"] += monster["gold"]

    # ⬆️ LEVEL UP
    level_up_text = ""
    required = get_required_xp(player["level"])

    while player["xp"] >= required:
        player["xp"] -= required
        player["level"] += 1
        player["stat_points"] += 5
        player["hp"] += 20
        required = get_required_xp(player["level"])

        level_up_text += (
            f"\n\n🎉 LEVEL UP!"
            f"\nLevel: {player['level']}"
            f"\n+5 stat points"
        )

    # 📝 TEXT
    text = (
        f"⚔ HUNT STARTED\n\n"
        f"👾 {monster['name']} ({monster['rank']})\n"
        f"❤️ HP: {monster['hp']}\n\n"
        f"💥 Damage: {damage}\n"
        f"❤️ Enemy Left: {max(0, monster_hp_left)}\n\n"
        f"🎁 Rewards:\n"
        f"+{monster['xp']} XP\n"
        f"+{monster['gold']} Gold"
        f"{level_up_text}"
    )

    # 🖼 IMAGE SYSTEM
    image_path = f"images/{monster['name'].lower().replace(' ', '_')}.jpg"

    try:
        await update.message.reply_photo(
            photo=open(image_path, "rb"),
            caption=text
        )
    except:
        await update.message.reply_text(text)

    # 🔥 SAVE FINAL DATA
    update_user(user.id, player)
