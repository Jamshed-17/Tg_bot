import telebot
bot = telebot.TeleBot("7136769737:AAEZhLglJIQtGr88HEjqUW8sfx2lYglVHAo")
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

bot.infinity_polling()

#Оно работает!!!!!!