from telegram import Update
from telegram.ext import ContextTypes
import random

async def enter_dungeon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    monsters = ["Goblin", "Skeleton", "Dark Wolf"]
    monster = random.choice(monsters)

    await update.message.reply_text(
        f"⚔️ You entered the dungeon!\n"
        f"A wild {monster} appeared!"
    )
