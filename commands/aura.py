from telegram import Update
from telegram.ext import ContextTypes

# Simple player aura data (future me DB me migrate kar sakte)
players_aura = {}

def get_player_aura(user_id):
    if user_id not in players_aura:
        players_aura[user_id] = {
            "current_aura": "None",
            "effects": {}
        }
    return players_aura[user_id]

# Aura stats example
auras = {
    "Flame": {"Attack": 5, "Defense": 0},
    "Shield": {"Attack": 0, "Defense": 5},
    "Storm": {"Attack": 3, "Defense": 2},
    "Healing": {"HP Regen": 5}
}

async def aura(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = get_player_aura(user.id)

    # Agar /setaura command ke sath aaya
    if context.args:
        aura_name = " ".join(context.args)
        if aura_name in auras:
            player["current_aura"] = aura_name
            player["effects"] = auras[aura_name]
            await update.message.reply_text(
                f"✨ Aura set to {aura_name}!\n"
                f"Effects: {player['effects']}"
            )
        else:
            await update.message.reply_text(
                f"❌ Aura '{aura_name}' does not exist.\n"
                f"Available auras: {', '.join(auras.keys())}"
            )
        return

    # Show current aura
    await update.message.reply_text(
        f"💫 Current Aura: {player['current_aura']}\n"
        f"Effects: {player['effects']}"
    )
