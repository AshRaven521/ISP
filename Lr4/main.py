import logging
import threading
import time

import schedule

from app import database, app
from config import TOKEN
from models import User, Link
from text_constants import START_MESSAGE
from vid_utils import Video, BadLink
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, Update
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
user_password = ""
user_name = ""
user_id = 0
ready_to_reference = False
ready_to_password = False
ready_to_reg = False
message_main = ""

bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

def bot_load():
    executor.start_polling(dispatcher)

@dispatcher.message_handler(state='*', content_types=ContentType.ANY)
async def handle_message(message: Message):
    global ready_to_reference
    global ready_to_reg
    global ready_to_password
    global user_id
    global user_password
    global message_main
    message_main = message
    if ready_to_reference == False:
        if message.text == "/start":
            await bot.send_message(chat_id=message.chat.id, text=START_MESSAGE)
            user_par = find_user_in_database(message.chat.username)
            if user_par:
                user_id = user_par[0]
                user_password = user_par[1]
            ready_to_password = True
        else:
            if message.text == "/reg":
                ready_to_reg = True
                ready_to_password = False
                ready_to_reference = False
                await bot.send_message(chat_id=message.chat.id, text="Please, enter your new password.")
            else:
                if ready_to_reg == True:
                    user_par = find_user_in_database(message.chat.username)
                    if user_par[0] == 0:
                        add_user_to_database(message.chat.username, message.text)
                        ready_to_reg = False
                    else:
                        ready_to_reg = False
                        await bot.send_message(chat_id=message.chat.id,
                                        text="You are in base already. Enter '/start' please!")
            if ready_to_password == True:
                if message.text == user_password:
                    ready_to_reference = True
                    await bot.send_message(chat_id=message.chat.id,
                                    text=f"Nice to see you, {message.chat.username}! Please, input the reference.")
                    if message.chat.username == "Cherrduck":
                        await admin_detected()
                else:
                    user_id = ""
                    user_password = ""
                    ready_to_reference = False
                    ready_to_password = False
                    await bot.send_message(chat_id=message.chat.id, text="Bad password. Enter '/start' again!")
            else:
                if ready_to_reg == False:
                    await bot.send_message(chat_id=message.chat.id, text="Please, enter '/start'")
    else:
        await get_format()

async def get_format():
    logger.info("from {}: {}".format(message_main.chat.id, message_main.text))

    try:
        video = Video(message_main.text, init_keyboard=True)
        find_link_in_database(message_main.text, user_id)
    except BadLink:
        await message_main.answer("Bad link")
    else:
        reply_markup = video.keyboard
        await message_main.answer('Choose format:', reply_markup=reply_markup)

@dispatcher.callback_query_handler()
async def download_chosen_format(call: CallbackQuery):
    resolution_code, link = call.data.split(' ', 1)
    if resolution_code != "id":
        await bot.edit_message_text(text="Downloading...", chat_id=call.message.chat.id, message_id=call.message.message_id)
        video = Video(link)
        video.download(resolution_code)
        with video.send() as files:
            for f in files:
                await bot.send_document(chat_id=call.message.chat.id, document=open(f, 'rb'))
    else:
        delete_user_from_db(link)
        await admin_detected()

def add_user_to_database(username, password):
    user = User(username, password)
    database.session.add(user)
    database.session.commit()
    global user_id
    user_id = user.id
    return user_id

def find_user_in_database(username):
    user = database.session.query(User).filter(User.username == f'{username}').all()
    if user:
        user_id = user[0].id
        user_password = user[0].password
    else:
        user_id = 0
        user_password = ""
    return [user_id, user_password]

def delete_user_from_db(userid):
    database.session.query(User).filter(User.id == f'{userid}').delete()
    database.session.commit()

def add_link_to_database(name, user_id):
    link = Link(name, user_id)
    database.session.add(link)
    database.session.commit()

def find_link_in_database(name, user_id):
    add_link_to_database(name, user_id)

async def admin_detected():
    user = User.query.all()
    if user:
        kb = InlineKeyboardMarkup()
        for us in user:
            kb.add(InlineKeyboardButton("{0}".format(us.username),
                                            callback_data="{} {}".format("id", us.id)))
        await message_main.answer('\nAdmin panel.\nChoose user for delete:', reply_markup=kb)

async def notification_sending():
    await bot.send_message(chat_id=message_main.chat.id,
                               text="Visit us more often!\nWe will be glad to see you!")

def scheduleOn():
    schedule.every().day.at("22:19").do(notification_sending)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    bot_load()
    thread = threading.Thread(target=scheduleOn)
    thread.start()
