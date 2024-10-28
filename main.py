from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from handlers.clear import clear
from handlers.start import start
from handlers.user_message import handle_message

# pip install python-telegram-bot
# pip install instaloader

TELEGRAM_TOKEN = "7507368634:AAECtEFDZ8dFD2_iapHcVJQZ0z6FjFzSmq4"
DOWNLOAD_DIR = "memes"
ONLINE_MESSAGE = "TG BOT - Online"

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    print(ONLINE_MESSAGE)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()
