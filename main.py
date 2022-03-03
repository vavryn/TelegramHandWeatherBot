import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
bot = telebot.TeleBot('5201792165:AAFQ9tWZcPgas9C3dpwIrkPsh7DRWcLWjdM')
r = requests.get('https://sinoptik.ua/погода-хмельницкий')
html = BS(r.content, 'html.parser')
for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Khmel = types.KeyboardButton('Хмельницкий')
    markup.add(Khmel)
    bot.send_message(message.chat.id, 'Напишите, с какого города Украины Вы хотите узнать погоду', reply_markup=markup)

@bot.message_handler(commands=['about'])
def about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, 'Связь с разработчиком данного бота \n Instagrаm - @elatedkrai  (https://www.instagram.com/elatedkrai/) \n Telegram - ElatedKrai (http://t.me/ElatedKrai)',reply_markup=markup)
    b = types.KeyboardButton('Вернуться к боту')
    markup.add(b)
    if message.text == 'Связь':
        bot.send_message(message.chat.id, '/start')

@bot.message_handler(content_types=['text'])
def weather(message):
    if message.chat.type == 'private':
        if message.text == 'Хмельницкий':
            bot.send_message(message.chat.id, '<b>Погода на ближайший день в Хмельницком:</b>' +' \n'+ t_min +' и '+ t_max+ '\n' + text ,parse_mode='html')
        else:
            bot.send_message (message.chat.id, 'Корректно напишите свой город')


bot.polling(none_stop=True)
