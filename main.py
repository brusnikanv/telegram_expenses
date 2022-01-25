import telebot
from telebot import types

bot = telebot.TeleBot('5023997839:AAGnjQoq9D9BLG-tINRVLYMU0EQQNyob9JM')
chat_id = "-757034015"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Hi")
# keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Main Menu")

    markup.add(item1)
    bot.send_message(message.chat.id, "Make Chose", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def input_chat(message):
    if message.chat.type == 'prive':
        if message.text == 'Main Menu':
            bot.send_message(message.chat.id, "rere")
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
#

bot.polling(none_stop=True)
