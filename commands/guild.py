from telegram import Update
from telegram.ext import ContextTypes
from database.db import users

# Simple guild storage (future me DB)
guilds = {}

async def createguild(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Agar command me guild name diya
    if context.args:
        guild_name = " ".join(context.args)

        if guild_name in guilds:
            await update.message.reply_text(f"❌ Guild '{guild_name}' already exists!")
            return

        guilds[guild_name] = {
            "owner": user.first_name,
            "members": [user.first_name]
        }

        await update.message.reply_text(
            f"🏰 Guild '{guild_name}' created successfully!\n"
            f"Owner: {user.first_name}\n"
            f"Members: {', '.join(guilds[guild_name]['members'])}"
        )
    else:
        # Show all guilds
        if not guilds:
            await update.message.reply_text("❌ No guilds created yet.")
            return

        guild_list = "🏰 Guilds:\n"
        for g_name, g_data in guilds.items():
            guild_list += f"{g_name} - Owner: {g_data['owner']} - Members: {len(g_data['members'])}\n"
        await update.message.reply_text(guild_list)
