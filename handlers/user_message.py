from telegram import Update
from telegram.ext import ContextTypes
import re
import instaloader
import os


def _extract_id(url: str) -> str:
    match = re.search(r'https?://www\.instagram\.com/(?:p|reel)/([^/]+)/?', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Unable to extract post id from URL")


def _download_media(shortcode, base_directory):
    loader = instaloader.Instaloader()
    
    target_directory = os.path.join(base_directory, shortcode)
    os.makedirs(target_directory, exist_ok=True)

    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target=target_directory)

    print(f"== Downloaded {shortcode} to {target_directory}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text

    try:
        post_id = _extract_id(url)
        _download_media(post_id, "memes")
        await update.message.reply_text(f'Successfully downloaded post with id {post_id}')
    except ValueError as e:
        print(f"++ Unable to extract post id from message: {url}")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"++ Error occurred with Instaloader : {e}")
    except Exception as e:
        print(f'++ An unexpected error occurred. Error: {e}')
    finally:
        await update.message.reply_text('Invalid URL! Please send a valid Instagram post or reel URL.')
