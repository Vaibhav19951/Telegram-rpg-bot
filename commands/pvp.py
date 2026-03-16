async def challenge(update, context):
    if not context.args:
        await update.message.reply_text("Usage: /challenge @username")
        return

    opponent = context.args[0]

    await update.message.reply_text(
        f"⚔ PvP Challenge Sent!\n\n"
        f"Opponent: {opponent}\n"
        f"Battle mode will be added in the next step."
    )
