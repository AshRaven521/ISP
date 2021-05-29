import logging

from telegram import InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters

from vid_utils import Video, BadLink

from app import database, app
from models import User, Link
from config import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def get_format(bot, update):
    logger.info("from {}: {}".format(update.message.chat_id, update.message.text))

    try:
        video = Video(update.message.text, init_keyboard=True)
        #user_id=find_user_in_database(update.message.chat.username, update.message.chat_id)
        user_id = find_user_in_database("Valera", 1333)
        find_link_in_database(update.message.text, user_id)
    except BadLink:
        update.message.reply_text("Bad link")
    else:
        reply_markup = InlineKeyboardMarkup(video.keyboard)
        update.message.reply_text('Choose format:', reply_markup=reply_markup)


def download_chosen_format(bot, update):
    query = update.callback_query
    resolution_code, link = query.data.split(' ', 1)
    
    bot.edit_message_text(text="Downloading...",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

    video = Video(link)
    video.download(resolution_code)
    
    with video.send() as files:
        for f in files:
            bot.send_document(chat_id=query.message.chat_id, document=open(f, 'rb'))


def add_user_to_database(username):
    data = User(username)
    database.session.add(data)
    database.session.commit()
    user_id = data.id
    return user_id

def find_user_in_database(username, id):
    user = database.session.query(User).filter(User.username == f'{username}').all()
    if not user:
        user_id = add_user_to_database(username)
    else:
        user_id = user[0].id
    return user_id

def add_link_to_database(name, user_id):
    link = Link(name, user_id)
    database.session.add(link)
    database.session.commit()

def find_link_in_database(name, user_id):
    #link = database.session.query(Link).filter(Link.name == f'{name}', Link.user_id == f'{user_id}').all()
    #if not link:
    add_link_to_database(name, user_id)




updater = Updater(token = TOKEN, use_context=False)

updater.dispatcher.add_handler(MessageHandler(Filters.text, get_format))
updater.dispatcher.add_handler(CallbackQueryHandler(download_chosen_format))


updater.start_polling()
updater.idle()

if __name__ == '__main__':
    app.run()
