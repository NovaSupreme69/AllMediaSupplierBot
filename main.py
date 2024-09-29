from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging
import requests
import os
import threading

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Example media source URLs (replace these with your actual media source)
MEDIA_SOURCE_URLS = {
    "book": "https://annas-archive.li/",
    "comic": "https://comixextra.com/",
    "anime": "https://123anime.info/home",
    "webseries": "https://123movieshdd.com/home/",  
    "manga": "https://mangareader.to/",
    "manhwa": "https://manganato.com/",
    "manhua": "https://manganato.com/",
    "lightnovel": "https://novelbuddy.com/home",
    "movie": "https://123anime.info/home",  
    "music": "https://streamsquid.com/#/browse/newrel"  
}

def fetch_media(media_type: str, name: str):
    """
    Downloads media to Render's server and returns the path.
    
    :param media_type: Type of media (book, comic, anime, etc.)
    :param name: Name of the media
    :return: Path to the media file if downloaded successfully; otherwise None
    """
    
    # Construct the URL based on media type (custom logic may be needed)
    if media_type in MEDIA_SOURCE_URLS:
        file_url = f"{MEDIA_SOURCE_URLS[media_type]}search?q={name.replace(' ', '+')}"  # Example search URL
        file_path = f"/tmp/{name.lower().replace(' ', '_')}.pdf" if media_type != 'music' else f"/tmp/{name.lower().replace(' ', '_')}.mp3"

        try:
            # Simulate downloading the file (replace with actual download logic)
            response = requests.get(file_url)
            response.raise_for_status()  # Raise an error for bad responses

            # Write the content to a file (mock implementation)
            with open(file_path, 'wb') as file:
                file.write(response.content)

            logging.info(f"Downloaded {media_type} '{name}' successfully.")
            return file_path  # Return the path if download was successful

        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading {media_type} '{name}': {e}")
            return None  # Return None if there was an error
    else:
        logging.error(f"Media type '{media_type}' not recognized.")
        return None

def start(update: Update, context: CallbackContext) -> None:
    commands = "/start - Start the bot\n" \
               "/help - Get help\n" \
               "/book <book name> - Get a book in PDF format\n" \
               "/comic <comic name> - Get a comic in PDF format\n" \
               "/anime <anime name> - Get anime episodes\n" \
               "/webseries <web series name> - Get web series episodes\n" \
               "/manga <manga name> - Get manga chapters\n" \
               "/manhwa <manhwa name> - Get manhwa chapters\n" \
               "/manhua <manhua name> - Get manhua chapters\n" \
               "/LightNovel <light novel name> - Get light novel chapters\n" \
               "/movie <movie name> - Get a movie\n" \
               "/music <music name> - Get a music track"\
               "if the bot can't provide a particular "\
               "anime/book/movie/series/manga/manhwa/manhua/LN/music. Send the name of the media (specify what it is) "\
                 "on the channel https://t.me/+84OqFZlkcVEwMWI1"
    update.message.reply_text(f"List of Commands:\n{commands}")

def help_command(update: Update, context: CallbackContext) -> None:
    help_text = ("Contact @UWUCHIHA69 if facing any bugs/issues or if the bot can't provide a particular "
                 "anime/book/movie/series/manga/manhwa/manhua/LN/music. Send the name of the media (specify what it is) "
                 "on the channel https://t.me/+84OqFZlkcVEwMWI1 (NOTE- CURRENTLY MOVIES ARE ONLY AVAILABLE IN 720p).")
    update.message.reply_text(help_text)

def schedule_deletion(context: CallbackContext, chat_id: int, message_id: int):
   """Delete a message from Telegram after 5 minutes."""
   threading.Event().wait(300)  # Wait for 5 minutes
   context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def delete_media(file_path: str):
   """Delete the local media file."""
   if os.path.isfile(file_path):
       os.remove(file_path)

def book(update: Update, context: CallbackContext) -> None:
    book_name = ' '.join(context.args)
    
    pdf_path = fetch_media("book", book_name)
    
    if pdf_path and os.path.isfile(pdf_path):
        with open(pdf_path, 'rb') as file:
            message = update.message.reply_document(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(pdf_path)

def comic(update: Update, context: CallbackContext) -> None:
    comic_name = ' '.join(context.args)
    
    pdf_path = fetch_media("comic", comic_name)
    
    if pdf_path and os.path.isfile(pdf_path):
        with open(pdf_path, 'rb') as file:
            message = update.message.reply_document(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(pdf_path)

def anime(update: Update, context: CallbackContext) -> None:
    anime_name = ' '.join(context.args)
    
    # Logic to fetch and send anime episodes would go here
    update.message.reply_text(f"Fetching anime: {anime_name}...")

def webseries(update: Update, context: CallbackContext) -> None:
    webseries_name = ' '.join(context.args)
    
    # Logic to fetch and send web series episodes would go here
    update.message.reply_text(f"Fetching web series: {webseries_name}...")

def manga(update: Update, context: CallbackContext) -> None:
    manga_name = ' '.join(context.args)
    
    pdf_path = fetch_media("manga", manga_name)
    
    if pdf_path and os.path.isfile(pdf_path):
        with open(pdf_path, 'rb') as file:
            message = update.message.reply_document(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(pdf_path)

def manhwa(update: Update, context: CallbackContext) -> None:
    manhwa_name = ' '.join(context.args)
    
    pdf_path = fetch_media("manhwa", manhwa_name)
    
    if pdf_path and os.path.isfile(pdf_path):
        with open(pdf_path, 'rb') as file:
            message = update.message.reply_document(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(pdf_path)

def manhua(update: Update, context: CallbackContext) -> None:
    manhua_name = ' '.join(context.args)
    
    pdf_path = fetch_media("manhua", manhua_name)
    
    if pdf_path and os.path.isfile(pdf_path):
        with open(pdf_path, 'rb') as file:
            message = update.message.reply_document(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(pdf_path)

def light_novel(update: Update, context: CallbackContext) -> None:
    light_novel_name = ' '.join(context.args)
    
    pdf_path = fetch_media("lightnovel", light_novel_name)
    
    if pdf_path and os.path.isfile(pdf_path):
        with open(pdf_path, 'rb') as file:
            message = update.message.reply_document(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(pdf_path)

def movie(update: Update, context: CallbackContext) -> None:
    movie_name = ' '.join(context.args)
    
    video_path = fetch_media("movie", movie_name)
    
    if video_path and os.path.isfile(video_path):
        with open(video_path, 'rb') as file:
            message = update.message.reply_video(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(video_path)

def music(update: Update, context: CallbackContext) -> None:
    music_name = ' '.join(context.args)
    
    music_file_path = fetch_media("music", music_name)
    
    if music_file_path and os.path.isfile(music_file_path):
        with open(music_file_path, 'rb') as file:
            message = update.message.reply_audio(file)

        threading.Thread(target=schedule_deletion, args=(context, update.message.chat_id, message.message_id)).start()
        
        delete_media(music_file_path)

def button_handler(update: Update, context: CallbackContext):
   query = update.callback_query
   query.answer()
   
   # Logic to handle button presses based on callback data
   media_type_quality = query.data.split('_')
   media_type = media_type_quality[0]
   quality = media_type_quality[1]

   if media_type.startswith("anime"):
       query.edit_message_text(text=f"Fetching {media_type} in {quality} quality...")
   
   elif media_type.startswith("webseries"):
       query.edit_message_text(text=f"Fetching {media_type} in {quality} quality...")

from flask import Flask, request

app = Flask(__name__)

def main():
    # Initialize the Updater and Dispatcher for the bot
    updater = Updater("Y7534687871:AAHJqUKnNdB4JLGsDnc3miajomFu-VqEGFQ", use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers as before
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("book", book))
    dispatcher.add_handler(CommandHandler("comic", comic))
    dispatcher.add_handler(CommandHandler("anime", anime))
    dispatcher.add_handler(CommandHandler("webseries", webseries))
    dispatcher.add_handler(CommandHandler("manga", manga))
    dispatcher.add_handler(CommandHandler("manhwa", manhwa))
    dispatcher.add_handler(CommandHandler("manhua", manhua))
    dispatcher.add_handler(CommandHandler("LightNovel", light_novel))
    dispatcher.add_handler(CommandHandler("movie", movie))
    dispatcher.add_handler(CommandHandler("music", music))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    # Webhook URL for Render
    HEROKU_APP_NAME = "allmediasupplierbot"  # Replace this with your Render app name
    PORT = int(os.environ.get('PORT', '8443'))  # Port number for Render

    webhook_url = f"https://{allmediasupplierbot}.onrender.com/{updater.bot.token}"

    # Set the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=updater.bot.token,
                          webhook_url=webhook_url)

    # Start Flask app
    app.run(port=PORT, debug=True)

@app.route(f'/{updater.bot.token}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return 'ok'
