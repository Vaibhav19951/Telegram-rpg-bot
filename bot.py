import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update, context):
    await update.message.reply_text("🤖 RPG Bot is running!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()
