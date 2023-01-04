import os

import telebot
from telebot import types

from config import BOT_TOKEN
from converter_function import converter_voice_msg
from spotify_api import get_top_songs
from state_tree.base_state import BaseState
from state_tree.settings import Settings
from state_tree.start import Start, Authorization

bot = telebot.TeleBot(BOT_TOKEN)
clients_state = {}
spotify_link = ''

@bot.message_handler(commands=["start"])
def start_bot(message):

    clients_state[message.chat.id] = Start()
    bot_processing(message.chat.id)

    import sqlite3
    with sqlite3.connect("FFeelMusicClients.db") as connection:
        c = connection.cursor()
        is_in_database = c.execute("SELECT EXISTS(SELECT 1 FROM Clients WHERE Id=?)", (message.from_user.id,)).fetchone()

        if is_in_database == (1,):
            clients_state[message.chat.id] = clients_state[message.chat.id].process(mark=True)
        else:
            clients_state[message.chat.id] = clients_state[message.chat.id].process()


    bot_processing(message.chat.id)

def bot_processing(chat_id):
    current_state: BaseState = clients_state.get(chat_id, Start())
    #print(clients_state[chat_id])
    markup = types.InlineKeyboardMarkup()

    for button_msg, button_cmd in current_state.buttons:
        markup.add(types.InlineKeyboardButton(text=button_msg, callback_data=button_cmd))

    bot.send_message(chat_id, current_state.msg, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    current_state: BaseState = clients_state.get(call.message.chat.id, Start())
    new_state: BaseState = current_state.process(txt=call.data)
    clients_state[call.message.chat.id] = new_state
    bot_processing(call.message.chat.id)


@bot.message_handler(content_types=["text"])
def message_handler(message):
    current_state: BaseState = clients_state.get(message.chat.id, Start())
    print(current_state)
    new_state: BaseState = current_state.process(txt=message.text)
    clients_state[message.chat.id] = new_state


    if clients_state[message.chat.id] == Settings():
        import sqlite3
        with sqlite3.connect("FFeelMusicClients.db") as connection:
            c = connection.cursor()
            c.execute("UPDATE Clients SET ? WHERE Id=?", (message.text, message.from_user.id, ))

    if message.text.startswith('http'):
        global spotify_link
        spotify_link = message.text

    if message.text.isnumeric():
        for artist, song in get_top_songs(spotify_link, message.text).items():
            bot.send_message(message.chat.id, f'{artist} - {song}')


    if message.text.startswith('+380') and clients_state[message.chat.id] == Authorization():
        import sqlite3
        with sqlite3.connect("FFeelMusicClients.db") as connection:
            params = (message.from_user.id, message.from_user.first_name, message.from_user.username, message.text)
            c = connection.cursor()
            c.execute(
                       "INSERT OR IGNORE INTO Clients"
                       "(Id, first_name, username, phone_number)"
                       "VALUES (?,?,?,?)", params)

        bot.send_message(message.chat.id, 'Успішно зареєстровано')

    bot_processing(message.chat.id)

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    print(message.voice)
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('voice_message.m4a', 'wb') as new_file:
        new_file.write(downloaded_file)

    converted = converter_voice_msg("voice_message.m4a")
    os.remove("voice_message.m4a")

    with open(converted, 'rb') as audio:
        bot.send_audio(message.chat.id, audio=audio)

    os.remove(converted)

if __name__ == '__main__':
    bot.infinity_polling()
