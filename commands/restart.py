import os
import sys
from database.db import users

# 🔥 MULTIPLE ADMINS
ADMIN_IDS = [2086993762, 7708811819]  # 👈 apne ids daal

async def restart(update, context):
    user = update.effective_user

    # ❌ Non-admin block
    if user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not allowed")
        return

    await update.message.reply_text("♻️ Restarting bot safely...")

    # 🧹 Clean shutdown (important)
    await context.application.shutdown()

    # 💀 SAFE RESTART
    os.execv(sys.executable, [sys.executable] + sys.argv)
