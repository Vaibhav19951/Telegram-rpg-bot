from telegram import Update
from telegram.ext import ContextTypes

# Simple map locations
locations = {
    "Village": "A peaceful village with friendly NPCs and a small shop.",
    "Dark Forest": "Beware! Monsters roam here. Adventure awaits.",
    "Dungeon Entrance": "Enter if you dare. Powerful bosses lurk inside.",
    "Mountain Pass": "A dangerous path with high rewards.",
    "Lake of Serenity": "A calm lake. Rest here to heal HP."
}

async def show_map(update: Update, context: ContextTypes.DEFAULT_TYPE):
    map_text = "🗺️ Available Locations:\n\n"
    for loc_name, desc in locations.items():
        map_text += f"• {loc_name} - {desc}\n"

    map_text += "\nUse /go <location> to move there (feature coming soon!)."
    
    await update.message.reply_text(map_text)
