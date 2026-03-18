from database.db import users
async def team(update, context):
    user = update.effective_user
    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("First use /start")
        return

    team_list = player.get("team", [])

    slots = []
    for i in range(3):
        if i < len(team_list):
            slots.append(f"{i+1}️⃣ {team_list[i]}")
        else:
            slots.append(f"{i+1}️⃣ Empty")

    await update.message.reply_text(
        "👥 YOUR TEAM\n\n" + "\n".join(slots)
    )
