from telegram import Update
from telegram.ext import CallbackContext

def clear(update: Update, context: CallbackContext) -> None:
    num_messages = int(context.args[0]) if context.args else 5  # Default to 5 if no number is provided
    chat_id = update.effective_chat.id

    message_ids = []
    for i in range(num_messages):
        message = context.bot.send_message(chat_id=chat_id, text="Temporary message to delete", reply_to_message_id=update.message.message_id)
        message_ids.append(message.message_id)

    for message_id in message_ids:
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)

    update.message.reply_text(f"Cleared {num_messages} messages!")