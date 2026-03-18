from systems.battle_system import calculate_damage
from database.db import users

async def pvp(update, context):
    user = update.effective_user
    players = context.bot_data.get("players", {})

    if user.id not in players:
        await update.message.reply_text("Use /start first.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /arena @username")
        return

    # Get opponent username
    opponent_username = context.args[0].replace("@", "")

    opponent = None
    opponent_id = None

    for uid, data in players.items():
        if data.get("username") == opponent_username:
            opponent = data
            opponent_id = uid
            break

    if not opponent:
        await update.message.reply_text("Opponent not found or not registered.")
        return

    attacker = players[user.id]
    defender = opponent

    # Simulate one round
    damage, crit = calculate_damage(attacker, defender, "basic")
    defender["hp"] -= damage

    result = f"⚔ PvP Battle ⚔\n\n"
    result += f"You attacked {opponent_username}\n"
    result += f"Damage: {damage}\n"

    if crit:
        result += "💥 CRITICAL HIT!\n"

    result += f"\nOpponent HP left: {defender['hp']}"

    if defender["hp"] <= 0:
        result += "\n\n🏆 You won the battle!"

    await update.message.reply_text(result)
