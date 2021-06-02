import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters, CommandHandler

from app import database, app
from config import TOKEN
from models import User, Link
from text_constants import START_MESSAGE
from vid_utils import Video, BadLink

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class MessageReact(object):
    user_password = ""
    user_name = ""
    mychat_id = 0
    user_id = 0
    ready_to_reference = False
    ready_to_password = False
    ready_to_reg = False
    password_default = "aaa"

    def __init__(self, bottoken):
        self.updater = Updater(token = bottoken, use_context=False)
        handler = MessageHandler(Filters.text | Filters.command, self.handle_message)
        self.updater.dispatcher.add_handler(handler)
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.download_chosen_format))

    def botload(self):
        self.updater.start_polling()

    def bot_starts(self, bot, update):
        bot.sendMessage(chat_id = update.message.chat_id, text = START_MESSAGE)

    def handle_message(self, bot, update):
        self.mychat_id = update.message.chat_id
        if self.ready_to_reference == False:
            if update.message.text == "/start":
                self.bot_starts(bot, update)
                user_par = self.find_user_in_database(update.message.chat.username)
                #user_par = self.find_user_in_database("Evgeniy")
                if user_par:
                    self.user_id = user_par[0]
                    self.user_password = user_par[1]
                #bot.sendMessage(chat_id = self.mychat_id, text="Password:")
                self.ready_to_password = True
            else:
                if update.message.text == "/reg":
                    bot.sendMessage(chat_id=self.mychat_id, text="Please, enter your new password.")
                    self.ready_to_reg = True
                    self.ready_to_password = False
                    self.ready_to_reference = False
                else:
                    if self.ready_to_reg == True:
                        user_par = self.find_user_in_database(update.message.chat.username)
                        if user_par[0] == 0:
                            self.add_user_to_database(update.message.chat.username, update.message.text)
                            self.ready_to_reg = False
                            #bot.sendMessage(chat_id=self.mychat_id, text="Enter '/start' now.")
                        else:
                            bot.sendMessage(chat_id=self.mychat_id, text="You are in base already. Enter '/start' please!")
                if self.ready_to_password == True:
                    if update.message.text == self.user_password:
                        bot.sendMessage(chat_id=self.mychat_id, text=f"Nice to see you, {update.message.chat.username}! Please, input the reference.")
                        self.ready_to_reference = True
                    else:
                        bot.sendMessage(chat_id=self.mychat_id, text="Bad password. Enter '/start' again!")
                        self.user_id = ""
                        self.user_password = ""
                        self.ready_to_reference = False
                        self.ready_to_password = False
                else:
                    if self.ready_to_reg == False:
                        bot.sendMessage(chat_id=self.mychat_id, text="Please, enter '/start'")
        else:
            self.get_format(bot, update)


    def get_format(self, bot, update):
        logger.info("from {}: {}".format(update.message.chat_id, update.message.text))

        try:
            video = Video(update.message.text, init_keyboard=True)
            self.find_link_in_database(update.message.text, self.user_id)
        except BadLink:
            update.message.reply_text("Bad link")
        else:
            reply_markup = InlineKeyboardMarkup(video.keyboard)
            update.message.reply_text('Choose format:', reply_markup = reply_markup)

    def download_chosen_format(self, bot, update):
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



    def add_user_to_database(self, username, password):
        user = User(username, password)
        database.session.add(user)
        database.session.commit()
        user_id = user.id
        return user_id

    def find_user_in_database(self, username):
        user = database.session.query(User).filter(User.username == f'{username}').all()
        if user:
            user_id = user[0].id
            user_password = user[0].password
        else:
            user_id = 0
            user_password = ""
        return [user_id, user_password]

    def add_link_to_database(self, name, user_id):
        link = Link(name, user_id)
        database.session.add(link)
        database.session.commit()

    def find_link_in_database(self, name, user_id):
        #link = database.session.query(Link).filter(Link.name == f'{name}', Link.user_id == f'{user_id}').all()
        #if not link:
        self.add_link_to_database(name, user_id)

if __name__ == "__main__":
    message_react = MessageReact(TOKEN)
    message_react.botload()





"""
def get_format(bot, update):
    logger.info("from {}: {}".format(update.message.chat_id, update.message.text))

    try:
        video = Video(update.message.text, init_keyboard=True)
        #user_id=find_user_in_database(update.message.chat.username, update.message.chat_id)
        user_id = find_user_in_database("Evgeniy", 1334)
        find_link_in_database(update.message.text, user_id)
    except BadLink:
        update.message.reply_text("Bad link")
    else:
        #btn1 = InlineKeyboardButton('Button', callback_data='button1')
        #kb1 = InlineKeyboardMarkup().add(btn1)
        markup = [[InlineKeyboardButton('Authorize', callback_data='a')]]
        update.message.reply_text('Authorize', reply_markup=InlineKeyboardMarkup(markup))
        #password_cheking(bot, update)
        #reply_markup = InlineKeyboardMarkup(video.keyboard)
        #update.message.reply_text('Choose format:', reply_markup=reply_markup)

#def process_command_button1(message: types.Message):
#    message.reply('Authorize', reply_markup = kb.kb1)


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


def add_user_to_database(username, password):
    user = User(username, password)
    database.session.add(user)
    database.session.commit()
    user_id = user.id
    return user_id

def find_user_in_database(username, password):
    user = database.session.query(User).filter(User.username == f'{username}').all()
    if not user:
        user_id = add_user_to_database(username, password)
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



def print_message(bot, update):
    update.callback_query.message.edit_text("Enter password:")

def password_cheking(bot, update):
    #update.callback_query.message.edit_text("Enter password:")
    #bot.sendMessage(update.message.chat_id, "Enter password:")
    user_password = update.message.from_user
    update.callback_query.message.edit_text(f'{user_password}')
    #return user_password
    #update.message.reply_text("Enter password:")
    #bot.sendMessage(chat_id = update.message.chat_id, text = "Enter password: ")
    #query = update.inline_query
    #text = query.query
    #query.from_user.send_message(text)
    try:
        user_password = update.message.text
    except:
        update.message.reply_text('Invalid password')




updater = Updater(token = TOKEN, use_context=False)

updater.dispatcher.add_handler(CommandHandler('start', bot_starts))
updater.dispatcher.add_handler(MessageHandler(Filters.text, get_format))
updater.dispatcher.add_handler(CallbackQueryHandler(print_message))
updater.dispatcher.add_handler(MessageHandler(Filters.text, password_cheking))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, password_cheking))
updater.dispatcher.add_handler(CallbackQueryHandler(download_chosen_format))


updater.start_polling()
updater.idle()

#if __name__ == '__main__':
    #app.run()
"""