from telegram import Update
from telegram.ext import ContextTypes

# Player data store (future me DB)
players = {}

def get_player(user_id, user_name):
    if user_id not in players:
        players[user_id] = {
            "name": user_name,
            "HP": 100,
            "Attack": 10,
            "Defense": 5,
            "Gold": 100,
            "inventory": ["Wooden Sword", "Health Potion"],
            "aura": "None"
        }
    return players[user_id]

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = get_player(user.id, user.first_name)

    profile_text = f"👤 Player Profile: {player['name']}\n\n"
    profile_text += f"❤️ HP: {player['HP']}\n"
    profile_text += f"⚔️ Attack: {player['Attack']}\n"
    profile_text += f"🛡 Defense: {player['Defense']}\n"
    profile_text += f"💰 Gold: {player['Gold']}\n"
    profile_text += f"💫 Aura: {player['aura']}\n"
    profile_text += f"🎒 Inventory: {', '.join(player['inventory'])}\n"

    await update.message.reply_text(profile_text)
