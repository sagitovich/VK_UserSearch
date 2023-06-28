import telebot

bot = telebot.TeleBot('5647652620:AAHRjYFJK_dxrwwoNZDp_quWcUTXtq1HkYc')

from telebot import types


@bot.message_handler(commands=['start'])  # Начало работы
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\n Хочешь кого-то найти?"  # Первое сообщение
    markup = types.InlineKeyboardMarkup()  # Создание кнопки как переменной
    button_yes = types.InlineKeyboardButton(text='Да',
                                            callback_data='yes')  # Текст кнопки и значение, которое принимает
    markup.add(button_yes)  # Добавление кнопки
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)  # Вывод всего что выше


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":  # Если нажали кнопку "Да"
            second_mess = "Напиши его id"  # Второе сообщение, после "Да"
            bot.send_message(function_call.message.chat.id, second_mess)  # Показать второе сообщение
            bot.answer_callback_query(function_call.id)  # Обработка команды закончена


from parser import parser_vk_id


@bot.message_handler(content_types=['text'])
def get_answer(message):
    third_mess = parser_vk_id(message.text)
    bot.send_message(message.chat.id, third_mess)  # Показать третье сообщение


bot.infinity_polling()
