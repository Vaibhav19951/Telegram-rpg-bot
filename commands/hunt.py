import random

MONSTERS = [
    {"name": "Goblin", "hp": 50, "xp": 20, "gold": 15},
    {"name": "Wolf", "hp": 60, "xp": 25, "gold": 20},
    {"name": "Orc", "hp": 80, "xp": 35, "gold": 30},
]

def get_required_xp(level: int) -> int:
    if level >= 30:
        return 30000
    return level * level * 100

async def hunt(update, context):
    user = update.effective_user
    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("First use /start")
        return

    monster = random.choice(MONSTERS)

    damage = player["strength"] * 5
    monster_hp_left = monster["hp"] - damage

    gained_xp = monster["xp"]
    gained_gold = monster["gold"]

    player["xp"] += gained_xp
    player["gold"] += gained_gold

    level_up_text = ""

    required = get_required_xp(player["level"])
    while player["xp"] >= required:
        player["xp"] -= required
        player["level"] += 1
        player["stat_points"] += 5
        player["hp"] += 20
        player["mana"] += 10
        required = get_required_xp(player["level"])
        level_up_text += (
            f"\n\n🎉 LEVEL UP!\n"
            f"You are now level {player['level']}.\n"
            f"+5 stat points gained."
        )

    await update.message.reply_text(
        f"⚔ HUNT STARTED\n\n"
        f"Enemy: {monster['name']}\n"
        f"Enemy HP: {monster['hp']}\n\n"
        f"You dealt {damage} damage.\n"
        f"Enemy HP left: {max(0, monster_hp_left)}\n\n"
        f"Rewards:\n"
        f"+{gained_xp} XP\n"
        f"+{gained_gold} Gold"
        f"{level_up_text}"
    )
