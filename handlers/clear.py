from telegram import Update
from telegram.ext import CallbackContext

def clear(update: Update, context: CallbackContext) -> None:
    num_messages = 0
    update.message.reply_text(f"Cleared {num_messages} messages! Feature coming soon.")