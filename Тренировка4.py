import telebot
import sqlite3
from telebot import types
bot = telebot.TeleBot("7136769737:AAEZhLglJIQtGr88HEjqUW8sfx2lYglVHAo")
name = '' #Создаём переменную, которая пригодится ниже***

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('botData.sql')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))")
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Привет. Я тебя регистрирую, введи своё имя")
    bot.register_next_step_handler(message, user_name)          # register_next_step_handler определяет функцию, которая будет запущена следующей


def user_name(message):
    global name     #Исподльзуем переменную, которую объявляли в начале кода, иначе переменная name будет существовать только внутри этой функции (а sql запрос с записью пользователя в другой функции)
    name = message.text.strip()     #...strip - удаляет различные пробелы в тексте
    bot.send_message(message.chat.id, "Введи пароль")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('botData.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()       #Исподльзуется для изменения значений в БД
    cur.close()
    conn.close()
    bot.register_next_step_handler(message, user_name)

    marcup = types.InlineKeyboardMarkup()
    marcup.add(types.InlineKeyboardButton("Список пользователей", callback_data="users"))
    bot.send_message(message.chat.id, "Ты зарегистрирован", reply_markup=marcup)

    # bot.send_message(message.chat.id, "Введи пароль")
    # bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('botData.sql')
    cur = conn.cursor()
    cur.execute("SELECT * from users")
    users = cur.fetchall()

    info = ""
    for i in users:
        info += f"Имя: {i[1]}, пароль: {i[2]}\n"

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)



bot.polling(none_stop=True)
