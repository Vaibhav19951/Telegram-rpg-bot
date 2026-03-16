async def start(update, context):
    user = update.effective_user

    # Ensure players storage exists
    if "players" not in context.bot_data:
        context.bot_data["players"] = {}

    players = context.bot_data["players"]

    # Already registered
    if user.id in players:
        await update.message.reply_text(
            "⚠ You are already registered.\nUse /profile to view your stats."
        )
        return

    # Register new player
    players[user.id] = {
        "username": user.username,  # Important for PvP
        "name": "Sung Jin-Woo",
        "rank": "E",
        "level": 1,
        "xp": 0,
        "gold": 100,
        "hp": 120,
        "mana": 40,
        "strength": 5,
        "vitality": 5,
        "agility": 5,
        "intelligence": 5,
        "sense": 5,
        "stat_points": 0,
        "aura": "light",   # Default aura
        "team": ["Sung Jin-Woo"],
        "hunters": ["Sung Jin-Woo"],
        "shadows": [],
        "summons": 0,
        "last_boss": None
    }

    await update.message.reply_text(
        "🗡 HUNTER REGISTERED!\n\n"
        "Name: Sung Jin-Woo\n"
        "Rank: E\n"
        "Level: 1\n"
        "Aura: LIGHT\n\n"
        "Use /profile to check your stats.\n"
        "Use /setaura to change aura."
    )
