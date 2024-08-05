import telebot
from telebot import types
bot = telebot.TeleBot("7136769737:AAEZhLglJIQtGr88HEjqUW8sfx2lYglVHAo")

@bot.message_handler(commands=['start'])
def start(message):
    button = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    button.row(btn1)
    btn2 = types.KeyboardButton('Удалить')
    btn3 = types.KeyboardButton('Изменить текст')
    button.row(btn2, btn3)
    file = open('./1.png', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=button)
    # bot.send_audio(message.chat.id, file, reply_markup=button)
    bot.send_message(message.chat.id, "Привет😃", reply_markup=button)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'open')
    elif message.text == 'Удалить':
        bot.send_message(message.chat.id, 'Ok')

@bot.message_handler(content_types=['photo'])           #Работает с различным контентом - например фото
def get_photo(message):
    button = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url="https://urtk-mephi.ru/pages.php?id=11")
    button.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    button.row(btn2, btn3)
    bot.reply_to(message, f"Какое красивое фото", reply_markup=button)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data=="edit":
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)




bot.polling(none_stop=True)