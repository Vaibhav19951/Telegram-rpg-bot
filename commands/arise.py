from telegram import Update
from telegram.ext import ContextTypes
from database.db import users


ARISEABLE_BOSSES = {
    "Blood-Red Commander Igris": "Igris",
    "Baruka": "Baruka",
    "Cerberus": "Cerberus",
    "Kargalgan": "Kargalgan",
    "Ant King": "Ant King",
}

PREMIUM_NOT_ARISE = {
    "Antares", "Ashborn", "Baran", "Rakan", "Sillad",
    "Tarnak", "Legia", "Querehsha", "Yogumunt"
}


async def arise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    # 🔥 USERS DATABASE CHECK
    player = users.get(user_id)

    if not player:
        await update.message.reply_text("❌ Pehle /start kar")
        return

    # 🔥 LAST BOSS CHECK
    boss = player.get("last_boss")

    if not boss:
        await update.message.reply_text("❌ No recent boss available for arise.")
        return

    # 🔥 PREMIUM CHECK
    if boss in PREMIUM_NOT_ARISE:
        await update.message.reply_text("❌ Ye boss arise nahi ho sakta")
        return

    # 🔥 ARISEABLE CHECK
    if boss not in ARISEABLE_BOSSES:
        await update.message.reply_text("❌ Ye boss ariseable nahi hai")
        return

    shadow_name = ARISEABLE_BOSSES[boss]

    # 🔥 INVENTORY ME ADD KARNA
    if "shadows" not in player:
        player["shadows"] = []

    player["shadows"].append(shadow_name)

    await update.message.reply_text(
        f"🔥 {boss} ko arise kar liya!\n\n"
        f"👤 Shadow: {shadow_name} added to your army 💀"
    )
