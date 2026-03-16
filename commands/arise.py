ARISEABLE_BOSSES = {
    "Blood-Red Commander Igris": "Igris",
    "Baruka": "Baruka",
    "Cerberus": "Cerberus",
    "Kargalgan": "Kargalgan",
    "Ant King": "Ant King",
}

PREMIUM_NOT_ARISE = {
    "Antares", "Ashborn", "Baran", "Rakan", "Sillad",
    "Tarnak", "Legia", "Querehsha", "Yogumunt"
}

async def arise(update, context):
    user = update.effective_user
    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("First use /start")
        return

    boss = player.get("last_boss")

    if not boss:
        await update.message.reply_text("No recent boss available for arise.")
        return

    if boss in PREMIUM_NOT_ARISE:
        await update.message.reply_text("❌ Premium monarchs cannot be obtained with arise.")
        return

    shadow = ARISEABLE_BOSSES.get(boss)
    if not shadow:
        await update.message.reply_text("❌ This boss cannot be turned into a shadow.")
        return

    if shadow in player["shadows"]:
        await update.message.reply_text(f"{shadow} is already in your shadow army.")
        return

    player["shadows"].append(shadow)
    await update.message.reply_text(
        f"🖤 ARISE!\n\n{boss} has been extracted as shadow.\n"
        f"New Shadow: {shadow}"
    )
