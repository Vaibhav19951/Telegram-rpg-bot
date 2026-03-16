async def start(update, context):
    user = update.effective_user

    # Temporary starter profile in memory
    if "players" not in context.bot_data:
        context.bot_data["players"] = {}

    players = context.bot_data["players"]

    if user.id not in players:
        players[user.id] = {
            "name": "Sung Jin-Woo",
            "rank": "E",
            "level": 1,
            "xp": 0,
            "hp": 120,
            "mana": 40,
            "gold": 100,
            "strength": 5,
            "vitality": 5,
            "agility": 5,
            "intelligence": 5,
            "sense": 5,
            "stat_points": 0,
            "team": ["Sung Jin-Woo"],
            "hunters": ["Sung Jin-Woo"],
            "shadows": [],
            "summons": 0,
            "last_boss": None
        }

        await update.message.reply_text(
            "🗡 Hunter Registered!\n\n"
            "Name: Sung Jin-Woo\n"
            "Rank: E\n"
            "Level: 1\n\n"
            "Use /profile to view your stats."
        )
    else:
        await update.message.reply_text(
            "You are already registered.\nUse /profile to check your hunter status."
        )
