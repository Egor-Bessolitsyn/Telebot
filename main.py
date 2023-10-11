from telebot import *
import sqlite3

bot = TeleBot('6537625140:AAG23LsPYtGPmbzgDRkDYFFhb_wsMZsmqdM')
user_name = ''


@bot.message_handler(commands=['start'])
def start(massage):
    bot.reply_to(massage, "Привет, пожалуйста, зарегистрируйся")
    bot.send_message(massage.chat.id, 'Введите имя')
    bot.register_next_step_handler(massage, name)


def name(message):
    global user_name
    user_name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, password)


def password(message: types.Message):
    global user_name
    id = message.from_user.id
    user_password = message.text.strip()
    conn = sqlite3.connect('Users.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Users (id, Name, Password) VALUES(?, ?, ?);''', (id, user_name, user_password))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Регистрация прошла успешно')


@bot.message_handler(commands=['help'])
def start(massege):
    bot.send_photo(massege.chat.id,
                   photo='https://vsthemes.org/uploads/posts/2021-10/1634974947_skrinshot-23-10-2021-12_40_48.webp',
                   caption=f"Здравствуйте, {massege.chat.first_name}, здесь вы сможете прочитать инфомацию о нашем боте")


@bot.message_handler(commands=['menu'])
def menu(message):
    murkup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/Show_password')
    btn2 = types.KeyboardButton('/Show_user_name')
    murkup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Доступные Вам функции', reply_markup=murkup)


bot.delete_webhook(drop_pending_updates=True)
bot.polling(none_stop=True)
