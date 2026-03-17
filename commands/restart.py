import os
import sys

ADMIN_ID = 2086993762  # 👈 apna telegram user id daal

async def restart(update, context):
    user = update.effective_user

    if user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not allowed")
        return

    await update.message.reply_text("♻️ Restarting bot...")

    os.execv(sys.executable, ['python'] + sys.argv)
