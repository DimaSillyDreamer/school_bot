import telebot

from config import *
import datetime
import time
from datetime import date
import numpy as numpy

bot = telebot.TeleBot(TOKEN)


def holidays_today(holidays, pub_holidays, delta_days):

    for k, v in pub_holidays.items():
        if v == (datetime.date.today() + datetime.timedelta(days=delta_days)):
            return k

    for k, v in holidays.items():
        if v[0] <= (datetime.datetime.now() + datetime.timedelta(days=delta_days)) <= v[1]:
            return k
        else:
            return lessons[(datetime.datetime.now() + datetime.timedelta(days=delta_days)).weekday()]


def how_much_days_to_the_end():
    holiday_1 = (numpy.busday_count(datetime.date(
        2022, 10, 29), datetime.date(2022, 11, 6)))
    holidays_2 = numpy.busday_count(datetime.date(
        2022, 12, 31), datetime.date(2023, 1, 8))
    holidays_3 = numpy.busday_count(datetime.date(
        2023, 4, 8), datetime.date(2023, 4, 16))

    return f'Осталось учиться до летних каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2023, 5, 27)) - holiday_1 - holidays_2 - holidays_3 - 7} д.'


def from_today_to_nearest_holidays():
    if datetime.date(2022, 9, 1) < datetime.date.today() < datetime.date(2022, 10, 29):
        return f'Осталось учиться до каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2022, 10, 29))} д.'
    elif datetime.date(2022, 10, 29) < datetime.date.today() < datetime.date(2022, 11, 6) or \
            datetime.date(2022, 12, 31) < datetime.date.today() < datetime.date(2023, 1, 8) or \
            datetime.date(2023, 4, 8) < datetime.date.today() < datetime.date(2023, 4, 16):
        return 'Уже каникулы!!!'
    elif datetime.date(2022, 11, 6) < datetime.date.today() < datetime.date(2022, 12, 31):
        return f'Осталось учиться до каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2022, 12, 31))} д.'
    elif datetime.date(2023, 1, 8) < datetime.date.today() < datetime.date(2023, 4, 8):
        return f'Осталось учиться до каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2023, 4, 8)) - 3} д.'
    elif datetime.date(2023, 4, 16) < datetime.date.today() < datetime.date(2023, 5, 27):

        return f'Осталось учиться до каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2023, 5, 27)) - 3} д.'


@bot.message_handler(commands=['start'])
def get_hello(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, {message.from_user.first_name}! Узнать расписание жми ⬇️MENU!')


@bot.message_handler(commands=['today'])
def question(message):
    bot.send_message(message.chat.id,
                     f"{holidays_today(holidays_periods, publick_holidays, 0)}")


@bot.message_handler(commands=['tomorrow'])
def question(message):
    bot.send_message(message.chat.id,
                     f"{holidays_today(holidays_periods, publick_holidays, 1)}")


@bot.message_handler(commands=['when_summer'])
def question(message):
    bot.send_message(message.chat.id,
                     how_much_days_to_the_end())


@bot.message_handler(commands=['when_holidays'])
def question(message):
    bot.send_message(message.chat.id,
                     from_today_to_nearest_holidays())


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
