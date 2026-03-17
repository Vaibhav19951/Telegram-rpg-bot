import random
from database.db import get_user, update_user


# 🎯 XP SYSTEM
def get_required_xp(level: int) -> int:
    if level >= 30:
        return 30000
    return level * level * 100


# 👾 MONSTERS (RANK BASED)
MONSTERS = [
    # E Rank
    {"name": "Goblin", "rank": "E", "hp": 50, "xp": 20, "gold": 15},
    {"name": "Wild Wolf", "rank": "E", "hp": 60, "xp": 25, "gold": 20},
    {"name": "Skeleton", "rank": "E", "hp": 55, "xp": 22, "gold": 18},

    # D Rank
    {"name": "Orc", "rank": "D", "hp": 80, "xp": 35, "gold": 30},
    {"name": "Lizardman", "rank": "D", "hp": 90, "xp": 40, "gold": 35},
    {"name": "Dark Mage", "rank": "D", "hp": 85, "xp": 45, "gold": 40},

    # C Rank
    {"name": "Ogre", "rank": "C", "hp": 120, "xp": 70, "gold": 60},
    {"name": "Shadow Beast", "rank": "C", "hp": 130, "xp": 75, "gold": 65},
    {"name": "Stone Golem", "rank": "C", "hp": 140, "xp": 80, "gold": 70},

    # B Rank
    {"name": "Demon Knight", "rank": "B", "hp": 180, "xp": 120, "gold": 100},
    {"name": "Frost Giant", "rank": "B", "hp": 200, "xp": 140, "gold": 120},
    {"name": "Hell Hound", "rank": "B", "hp": 190, "xp": 130, "gold": 110},

    # A Rank
    {"name": "Ancient Dragon", "rank": "A", "hp": 350, "xp": 300, "gold": 250},
    {"name": "Demon General", "rank": "A", "hp": 320, "xp": 280, "gold": 230},
    {"name": "Red Wyvern", "rank": "A", "hp": 300, "xp": 260, "gold": 220},
]


# 🔥 LEVEL BASED MONSTER PICK
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


# ⚔ MAIN HUNT
async def hunt(update, context):
    user = update.effective_user

    player = get_user(user.id)

    if not player:
        await update.message.reply_text("⚠️ First use /start")
        return

    monster = get_monster_by_level(player["level"])

    # ⚔ DAMAGE
    damage = player["strength"] * 5

    # 💥 CRIT
    crit = False
    crit_chance = player["sense"] * 0.01

    if random.random() < crit_chance:
        damage = int(damage * 1.5)
        crit = True

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

    crit_text = "\n💥 CRITICAL HIT!" if crit else ""

    caption_text = (
        f"⚔ HUNT STARTED\n\n"
        f"👾 Enemy: {monster['name']}\n"
        f"🏷 Rank: {monster['rank']}\n"
        f"❤️ HP: {monster['hp']}\n\n"
        f"💥 Damage: {damage}{crit_text}\n"
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
            caption=caption_text
        )
    except:
        await update.message.reply_text(caption_text)

    # 🔥 FINAL SAVE (MOST IMPORTANT)
    update_user(user.id, player)
