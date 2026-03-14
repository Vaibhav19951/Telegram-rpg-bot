from telegram import Update
from telegram.ext import ContextTypes

# Ye simple player data store (future me DB me migrate kar sakte)
players = {}

# Default player setup
def get_player(user_id, user_name):
    if user_id not in players:
        players[user_id] = {
            "name": user_name,
            "gold": 100,
            "inventory": ["Wooden Sword"],
        }
    return players[user_id]

# Shop items
shop_items = {
    "Health Potion": 20,
    "Iron Sword": 50,
    "Shield": 40,
    "Magic Scroll": 80
}

async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = get_player(user.id, user.first_name)

    # Agar /buy command ke sath aaya
    if context.args:
        item_name = " ".join(context.args)
        if item_name in shop_items:
            price = shop_items[item_name]
            if player["gold"] >= price:
                player["gold"] -= price
                player["inventory"].append(item_name)
                await update.message.reply_text(
                    f"✅ You bought {item_name} for {price} gold.\n"
                    f"💰 Remaining Gold: {player['gold']}"
                )
            else:
                await update.message.reply_text(
                    f"❌ You don't have enough gold for {item_name}."
                )
        else:
            await update.message.reply_text(f"❌ Item '{item_name}' not found in shop.")
        return

    # Show shop
    shop_text = "🏪 Welcome to the RPG Shop!\n\n"
    for item, price in shop_items.items():
        shop_text += f"{item} - {price} Gold\n"
    shop_text += f"\n💰 Your Gold: {player['gold']}\n"
    shop_text += "Use /shop <item_name> to buy an item."
    
    await update.message.reply_text(shop_text)
