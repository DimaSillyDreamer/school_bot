import telebot
from config import *
import datetime
import time
from telebot import types
import numpy as numpy


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_today = types.KeyboardButton('✏️ Расписание на сегодня 📚')
    button_tomorrow = types.KeyboardButton('🗓 Расписание на завтра 📋')
    button_summer_holidays = types.KeyboardButton(
        '🚀 Когда ближайшие каникулы 🚲')
    button_holidays = types.KeyboardButton('🏖 Когда летние каникулы ☀️')
    markup.add(button_today, button_tomorrow,
               button_summer_holidays, button_holidays)
    bot.send_message(message.chat.id, '🤖\nПривет!', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '✏️ Расписание на сегодня 📚')
def plan(message):
    bot.send_message(message.chat.id,
                     f"{holidays_today(holidays_periods, publick_holidays, 0)}")


@bot.message_handler(func=lambda message: message.text == '🗓 Расписание на завтра 📋')
def plan_tomorrow(message):
    bot.send_message(message.chat.id,
                     f"{holidays_today(holidays_periods, publick_holidays, 1)}")


@bot.message_handler(func=lambda message: message.text == '🚀 Когда ближайшие каникулы 🚲')
def holidays_soon(message):
    bot.send_message(message.chat.id,
                     from_today_to_nearest_holidays())


@bot.message_handler(func=lambda message: message.text == '🏖 Когда летние каникулы ☀️')
def holidays_soon(message):
    bot.send_message(message.chat.id,
                     how_much_days_to_the_end())


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
