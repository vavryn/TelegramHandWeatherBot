import telebot
import requests
from bs4 import BeautifulSoup as BS
bot = telebot.TeleBot('5201792165:AAFQ9tWZcPgas9C3dpwIrkPsh7DRWcLWjdM')
r = requests.get('https://sinoptik.ua/погода-хмельницкий')
html = BS(r.content, 'html.parser')

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

@bot.message_handler(commands=['weather'])
def weather(message): bot.send_message(message.chat.id, '<b>Погода на ближайший день в Хмельницком:</b>' +' \n'+ t_min +' и '+ t_max+ '\n' + text , parse_mode='html')

bot.polling(none_stop=True)
