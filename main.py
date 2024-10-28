from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.clear import clear
from handlers.start import start
from handlers.user_message import handle_message
from globals import load_config

# pip install python-telegram-bot
# pip install instaloader
# pip install toml

def main():
    global config
    config = load_config()

    TELEGRAM_TOKEN = config['telegram_token']
    BANNER = config['banner']

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    print(BANNER)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()