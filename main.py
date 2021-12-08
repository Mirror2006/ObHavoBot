import requests
import telebot
from config import *
from telebot import types

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('🔍 Search', 'ℹ️ About')

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    msg = f"<b>Assalomu aleykum {user} botga hush kelbsiz</b>"
    bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['search'])
def start(message):
    msg = f"<b>🔍 Enter a country or city name</b>"
    bot.send_message(message.chat.id, msg, parse_mode='html')

@bot.message_handler(content_types=['text'])
def weather(message):
    if message.text == '🔍 Search':
        msg = f"<b>🔍 Enter a country or city name</b>"
        bot.send_message(message.chat.id, msg, parse_mode='html')
    elif message.text == 'ℹ️ About':
        msg = f"""OpenWeather global xizmatlari.
Ob-havo prognozlari, joriy prognozlar va tarixni tez va oqlangan tarzda.
Biz hiperlokal ob-havo ma'lumotlarini har qanday biznes uchun ochiq qilamiz.
Dunyoning har bir nuqtasi uchun biz yorug'lik tezligida API orqali tarixiy, joriy va bashorat qilingan ob-havo ma'lumotlarini taqdim etamiz.
Global xizmatlar CreaterOpenWeather.
Ob-havo prognozlari, joriy prognozlar va tarixni tez va oqlangan tarzda.
Biz hiperlokal ob-havo ma'lumotlarini har qanday biznes uchun ochiq qilamiz.
Dunyoning har bir nuqtasi uchun biz yorug'lik tezligida API orqali tarixiy, joriy va bashorat qilingan ob-havo ma'lumotlarini taqdim etamiz.
yaratuvchi: @Mirjamol_rajabboyev"""
        bot.send_message(message.chat.id, msg, reply_markup=markup)

    else:
        try:
            CITY = message.text
            URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API}'
            response = requests.get(url=URL).json()
            city_info = {
                'city': CITY,
                'temp': response['main']['temp'],
                'humidity': response['main']['humidity'],
                'weather': response['weather'][0]['description'],
                'wind': response['wind']['speed'],
                'pressure': response['main']['pressure'],
            }
            msg = f"<b><u>{CITY.upper()}</u>\n\nWeather is {city_info['weather']}</b>\n------------------------------------\n🌡 Temperature: <b>{city_info['temp']} C</b>\n💨 Wind: <b>{city_info['wind']} m/s</b>\n💦 Humidity: <b>{city_info['humidity']} %</b>\n🧬 Pressure: <b>{city_info['pressure']} hPa</b>"
            bot.send_message(message.chat.id, msg, parse_mode='html')
        except:
            msg1 = f"<b>🙅‍♂️ Nothing found try again</b>"
            bot.send_message(message.chat.id, msg1, parse_mode='html')

bot.polling(none_stop=True)


