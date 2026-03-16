async def setaura(update, context):
    user = update.effective_user

    # Check player exists
    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("❌ First use /start to register.")
        return

    # No argument given
    if not context.args:
        await update.message.reply_text(
            "Usage: /setaura <type>\n\n"
            "Available Auras:\n"
            "🔥 fire\n"
            "💧 water\n"
            "⚡ lightning\n"
            "🌑 shadow\n"
            "✨ light"
        )
        return

    aura = context.args[0].lower()

    valid_auras = ["fire", "water", "lightning", "shadow", "light"]

    if aura not in valid_auras:
        await update.message.reply_text("❌ Invalid aura type.")
        return

    player["aura"] = aura

    await update.message.reply_text(
        f"✨ Aura successfully changed!\n\n"
        f"Current Aura: {aura.upper()}"
    )
