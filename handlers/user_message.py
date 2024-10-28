from telegram import Update
from telegram.ext import ContextTypes
import re
import instaloader
import os


def extract_id(url: str) -> str:
    match = re.search(r'https?://www\.instagram\.com/(?:p|reel)/([^/]+)/?', url)
    return match.group(1) if match else None


def download_media(shortcode, base_directory):
    loader = instaloader.Instaloader()
    
    target_directory = os.path.join(base_directory, shortcode)
    os.makedirs(target_directory, exist_ok=True)

    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target=target_directory)

    print(f"== Downloaded {shortcode} to {target_directory}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    post_id = extract_id(url)

    try:
        download_media(post_id, "memes")
    except Exception as e:
        print(f"++ ERROR : {e}")

    if post_id:
        await update.message.reply_text(f'Successfully downloaded post with id {post_id}')
    else:
        await update.message.reply_text('Invalid URL! Please send a valid Instagram post or reel URL.')
