async def profile(update, context):
    user = update.effective_user

    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("First use /start")
        return

    msg = (
        "🧾 HUNTER STATUS\n\n"
        f"Hunter: {player['name']}\n"
        f"Rank: {player['rank']}\n"
        f"Level: {player['level']}\n"
        f"XP: {player['xp']}\n"
        f"Gold: {player['gold']}\n\n"
        f"HP: {player['hp']}\n"
        f"Mana: {player['mana']}\n\n"
        f"Strength: {player['strength']}\n"
        f"Vitality: {player['vitality']}\n"
        f"Agility: {player['agility']}\n"
        f"Intelligence: {player['intelligence']}\n"
        f"Sense: {player['sense']}\n\n"
        f"Remaining Stat Points: {player['stat_points']}"
    )

    await update.message.reply_text(msg)
