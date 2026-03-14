from telegram import Update
from telegram.ext import ContextTypes

# Player data store (future me DB)
players = {}

def get_player(user_id, user_name):
    if user_id not in players:
        players[user_id] = {
            "name": user_name,
            "gold": 100,
            "inventory": ["Wooden Sword", "Health Potion"],
            "HP": 100,
            "Attack": 10,
            "Defense": 5
        }
    return players[user_id]

async def inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = get_player(user.id, user.first_name)

    inventory_text = f"🎒 {player['name']}'s Inventory:\n\n"
    if player["inventory"]:
        for idx, item in enumerate(player["inventory"], 1):
            inventory_text += f"{idx}. {item}\n"
    else:
        inventory_text += "Empty 😢\n"

    inventory_text += f"\n💰 Gold: {player['gold']}\n"
    inventory_text += f"❤️ HP: {player['HP']}\n"
    inventory_text += f"⚔️ Attack: {player['Attack']}\n"
    inventory_text += f"🛡 Defense: {player['Defense']}\n"

    await update.message.reply_text(inventory_text)
