from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.clear import clear
from handlers.start import start
from handlers.user_message import handle_message
import globals

# pip install python-telegram-bot
# pip install instaloader
# pip install toml

def main():
    globals.load_config()

    print(f"Logged as: {globals.USER}")

    app = ApplicationBuilder().token(globals.TELEGRAM_TOKEN).build()

    print(globals.BANNER)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()