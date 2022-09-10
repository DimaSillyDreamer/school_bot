
import numpy
import datetime


TOKEN = '5628978866:AAGUkxuTBwG-Gfdf7vixenQTQk76y3pToOc'

lessons = {
    0: f'📋Понедельник\n9:25 - 10:10 Русский язык\n10:30 - 11:15 Математика\n11:35 - 12:20 Английский язык\n12:30 - 13:15 Литературное чтение',
    1: f'📋Вторник\n8:30 - 9:15 Физ-ра\n9:25 - 10:10 Математика\n10:30 - 11:15 Русский язык\n11:35 - 12:20 Литературное чтение\n12:30 - 13:15 Музыка',
    2: f"📋Среда\n8:30 - 9:15 Английский язык\n9:25 - 10:10 Математика\n10:30 - 11:15 Литературное чтение\n11:35 - 12:20 Физ-ра",
    3: f'📋Четверг\n8:30 - 9:15 Математика\n9:25 - 10:10 Родной язык (русский)\n10:30 - 11:15 Литературное чтение\n11:35 - 12:20 Вокруг света с английским\n12:30 - 13:15 Технология',
    4: f'📋Пятница\n8:30 - 9:15 Русский язык\n9:25 - 10:10 Грамотный читатель\n10:30 - 11:15 Окружающий мир\n11:35 - 12:20 ИЗО\n12:30 - 13:15 Физ-ра',
    5: f'🥳 Cуббота!!! 🤩',
    6: f'🤩 Воскресенье!!! 🥳'
}

holidays_periods = {
    'Осенние каникулы': [datetime.datetime(2022, 10, 29), datetime.datetime(2022, 11, 6)],
    'Зимние каникулы': [datetime.datetime(2022, 12, 31), datetime.datetime(2023, 1, 8)],
    'Весенние каникулы': [datetime.datetime(2023, 4, 8), datetime.datetime(2023, 4, 16)]
}

publick_holidays = {
    'Новый год!': datetime.date(2023, 1, 1),
    'Рождество Христово': datetime.date(2023, 1, 7),
    'День защитника Отечества': datetime.date(2023, 2, 23),
    'Международный женский день': datetime.date(2023, 3, 8),
    'Праздник Весны и Труда': datetime.date(2023, 5, 1),
    'День Победы': datetime.date(2023, 5, 9),
    'День России': datetime.date(2023, 6, 12),
    'День народного единства': datetime.date(2022, 11, 4),
    'Нерабочий день к празднику: День защитника Отечества': datetime.date(2023, 2, 24),
    'Нерабочий день к празднику: День Победы': datetime.date(2023, 5, 8)
}


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

    return f'🤖 Учебных дней до летних каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2023, 5, 27)) - holiday_1 - holidays_2 - holidays_3 - 7}!!!'


def from_today_to_nearest_holidays():
    if datetime.date(2022, 9, 1) < datetime.date.today() < datetime.date(2022, 10, 29):
        return f'🤖 Учебных дней до ближайших каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2022, 10, 29))}!!!'
    elif datetime.date(2022, 10, 29) < datetime.date.today() < datetime.date(2022, 11, 6) or \
            datetime.date(2022, 12, 31) < datetime.date.today() < datetime.date(2023, 1, 8) or \
            datetime.date(2023, 4, 8) < datetime.date.today() < datetime.date(2023, 4, 16):
        return '🤖 Ура каникулы!!! 🥳'
    elif datetime.date(2022, 11, 6) < datetime.date.today() < datetime.date(2022, 12, 31):
        return f'🤖 Учебных дней до ближайших каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2022, 12, 31))}!!!'
    elif datetime.date(2023, 1, 8) < datetime.date.today() < datetime.date(2023, 4, 8):
        return f'🤖 Учебных дней до ближайших каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2023, 4, 8)) - 3}!!!'
    elif datetime.date(2023, 4, 16) < datetime.date.today() < datetime.date(2023, 5, 27):

        return f'🤖 Учебных дней до ближайших каникул: {numpy.busday_count(datetime.date.today(), datetime.date(2023, 5, 27)) - 3}!!!'
