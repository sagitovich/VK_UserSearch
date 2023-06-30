import telebot

bot = telebot.TeleBot('5647652620:AAHRjYFJK_dxrwwoNZDp_quWcUTXtq1HkYc')

from telebot import types


@bot.message_handler(commands=['start'])  # Начало работы
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\n Хочешь кого-то найти?"  # Первое сообщение
    markup = types.InlineKeyboardMarkup()  # Создание кнопки как переменной
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # Текст кнопки и значение, которое принимает
    markup.add(button_yes)  # Добавление кнопки
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)  # Вывод всего что выше


@bot.message_handler(commands=['help'])  # Команда хелп
def helpBot(message):
    help_mess = f"Вот команды, которые я умею:\n/start (Начало работы)\n/stop (Конец работы)\nТакже в мои возможности входит поиск людей во ВКонтакте.\nЧтобы найти человека напиши его id в VK"
    bot.send_message(message.chat.id, help_mess)


@bot.message_handler(commands=['stop'])  # Команда стоп
def stopBot(message):
    stop_mess = f"Уже закончили?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='end')
    button_no = types.InlineKeyboardButton(text='Нет', callback_data='yes')
    markup.add(button_yes, button_no)
    bot.send_message(message.chat.id, stop_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":  # Если нажали кнопку "Да"
            second_mess = "Напиши id человека, которого хочешь найти"  # Второе сообщение, после "Да"
            bot.send_message(function_call.message.chat.id, second_mess)  # Показать второе сообщение
            bot.answer_callback_query(function_call.id)  # Обработка команды закончена
        elif function_call.data == "end":
            end_mess = "До новых встреч!"
            bot.send_message(function_call.message.chat.id, end_mess)
            bot.answer_callback_query(function_call.id)


from vk_api_parser import vk_api_user


@bot.message_handler(content_types=['text'])
def get_answer(message):
    third_mess = vk_api_user(message.text)
    bot.send_message(message.chat.id, third_mess)  # Показать третье сообщение

for i in range(500, 601):
    vk_api_user(str(i))
    i = int(i)
    i += 1


bot.infinity_polling()
