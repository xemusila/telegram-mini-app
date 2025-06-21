from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = KeyboardButton(
        text="Открыть Mini App",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    await update.message.reply_text("Нажми кнопку ниже, чтобы открыть Mini App:", reply_markup=keyboard)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
