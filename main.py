from telebot import *

bot = TeleBot('6537625140:AAG23LsPYtGPmbzgDRkDYFFhb_wsMZsmqdM')


@bot.message_handler(commands=['start'])
def start(massege):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('1', url='https://ru.stackoverflow.com/questions/1354494/aiogram-ошибка-cant-parse-inline-keyboard-button-text-buttons-are-unallowed-in')
    btn2 = types.InlineKeyboardButton('2', callback_data='2')
    markup.add(btn1, btn2)
    bot.reply_to(massege, "Привет", reply_markup=markup)


@bot.message_handler(commands=['help'])
def start(massege):
    bot.reply_to(massege, f"Здравствуйте, {massege.chat.first_name}, здесь вы сможете прочитать инфомацию о нашем боте")


@bot.message_handler(commands=['markup'])
def start(massege):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('a')
    itembtnv = types.KeyboardButton('v')
    itembtnc = types.KeyboardButton('c')
    itembtnd = types.KeyboardButton('d')
    itembtne = types.KeyboardButton('e')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    bot.reply_to(massege, "Choose one letter:", reply_markup=markup)


bot.polling(none_stop=True)
