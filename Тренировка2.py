import telebot
import webbrowser #Здесь чтобы сразу открывать сайт

bot = telebot.TeleBot("7136769737:AAEZhLglJIQtGr88HEjqUW8sfx2lYglVHAo") #Переменная с токеном бота

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://urtk-mephi.ru/pages.php?id=11')

@bot.message_handler(commands=['start']) #Нужно, чтобы указать тригер для функции ниже
def first_message(message):
    bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name} {message.from_user.last_name}')
    #Выводит что-то (в скобках имя и фамилия пользователя)

@bot.message_handler(commands=['help'])
def first_message(message):
    bot.send_message(message.chat.id, 'Ну <b>допустим</b> чем то помогаю', parse_mode='html')

@bot.message_handler()          #Если здесь нет команды - ставить вниз, иначе другие работать не будут
def info(message):
    if message.text.lower() == 'привет':     #Lower - текст в нижнем регистре
        bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f"ID: {message.from_user.id}")      #reply_to - ответ на предыдущее сообщение

bot.polling(none_stop=True) #Нужно, чтобы программа работала постоянно