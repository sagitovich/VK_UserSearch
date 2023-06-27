import telebot

bot = telebot.TeleBot('5647652620:AAHRjYFJK_dxrwwoNZDp_quWcUTXtq1HkYc')

from telebot import types

@bot.message_handler(commands=['start']) #Начало работы
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, привет!\n Хочешь кого-то найти?" #Первое сообщение
  markup = types.InlineKeyboardMarkup() #Создание кнопки как переменной
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes') #Текст кнопки и значение, которое принимает
  markup.add(button_yes) #Добавление кнопки
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup) #Вывод всего выше перечисленного


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
      if function_call.message:
          if function_call.data == "yes": #Если нажали кнопку "Да"
              second_mess = "Напиши его id" #Второе сообщение, после "Да"
              bot.send_message(function_call.message.chat.id, second_mess) #Показать второе сообщение
              bot.answer_callback_query(function_call.id) #Обработка команды закончена

import requests
from bs4 import BeautifulSoup
@bot.message_handler(content_types=['text'])
def get_answer(message):
    url = "https://vk.com/" + message.text  # создание ссылки
    src = requests.get(url).text  # получаем html код страницы пользователя и переводим его в сплошной текст

    with open("index.html", "w") as file:  # открываем файл "index.html" для записи (он автоматически создаётся)
        file.write(src)  # записываем в него html код страницы пользователя

    with open("index.html") as file:  # открываем файл "index.html"
        src = file.read()  # считываем его в переменную src

    soup = BeautifulSoup(src, "lxml")  # создаём переменную, вызывая которую, можно собирать данные с файла

    exists = True
    try:
        user_name = soup.find(class_="op_header").text  # получаем имя пользователя и переводим его в текст
        third_mess_1 = "Имя пользователя: "
        third_mess_2 = f"{user_name.strip()}"
        third_mess = third_mess_1 + third_mess_2 #Получаем имя фамилию
    except:
        exists = False
        third_mess = "Пользователя с таким id не существует" # суть в том, что, если пользователя не существует, то паркер не найдёт таких данных, как "имя пользователя"
    bot.send_message(message.chat.id, third_mess)  # Показать второе сообщение


bot.infinity_polling()