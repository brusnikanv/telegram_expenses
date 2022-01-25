import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('5023997839:AAGnjQoq9D9BLG-tINRVLYMU0EQQNyob9JM')
chat_id = "-757034015"

@bot.message_handler(commands=['start'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("1️⃣All options")
	item2 = types.KeyboardButton("2️⃣Add bill")
	item3 = types.KeyboardButton("3️⃣Export xml")
	markup.row(item1)
	markup.row(item2, item3)
	bot.send_message(message.chat.id, "Выбери Пункт", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def inl_button(message):
	# inline_button
	if message.text == '2️⃣Add bill':
		cost_button = types.InlineKeyboardButton("cost", callback_data='cost')
		photo_button = types.InlineKeyboardButton("photo", callback_data='photo')
		markup = InlineKeyboardMarkup().row(cost_button, photo_button)
		bot.send_message(message.chat.id, 'Выбери пункт', reply_markup=markup)
	else:
		bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# RUN
bot.polling(none_stop=True)