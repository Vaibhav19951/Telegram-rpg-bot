async def start(update, context):
    user = update.effective_user

    # ❌ group block
    if update.effective_chat.type != "private":
        await update.message.reply_text(
            "⚠️ Use this bot in private chat only.\n👉 DM me to start!"
        )
        return

    from database.db import get_user, save_user

    player = get_user(user.id)

    # 🆕 NEW PLAYER
    if not player:
users[user_id] = {
    "name": update.effective_user.first_name,
    "rank": "E",
    "level": 1,
    "xp": 0,
    "gold": 100,

    "hp": 100,
    "mana": 50,

    "strength": 10,
    "vitality": 10,
    "agility": 10,
    "intelligence": 10,
    "sense": 10,

    "stat_points": 0,

    "inventory": [],
    "shadows": [],
    "aura": "None",
    "last_boss": None
}

        save_user(user.id, user.username, player)

        await update.message.reply_text(
            "✨ Welcome, Hunter!\n\n"
            "⚔️ Your journey begins now.\n"
            "💰 Gold: 100 | ❤️ HP: 100\n\n"
            "👉 Use /hunt"
        )

    # 🔁 OLD PLAYER
    else:
        await update.message.reply_text(
            f"👋 Welcome back!\n\n"
            f"🏆 Level: {player['level']}\n"
            f"💰 Gold: {player['gold']}\n"
            f"⚡ XP: {player['xp']}\n\n"
            f"👉 Use /hunt"
        )
