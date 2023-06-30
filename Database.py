# -*- coding: utf8 -*-
import sqlite3

def insert_varible_into_table(m_id, m_first_name, m_last_name, m_birth_date, m_city, m_phone_number, m_website):
    try:
        # Создаем подключение к базе данных
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        print("Подключен к SQLite")

        # Создаем таблицу users, если ее еще нет
        # conn.execute('''CREATE TABLE IF NOT EXISTS users
        #            (id INTEGER PRIMARY KEY,
        #             first_name TEXT,
        #             last_name TEXT,
        #             birth_date TEXT,
        #             city TEXT,
        #             phone_number TEXT,
        #             website TEXT);''')

        # Создаем запрос
        query = """INSERT INTO Users ('VK ID', Firstname, Lastname, 'Birth date', City, 'Phone number', Website) \
                        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        # Вставляем данные в таблицу
        data_tuple = (m_id, m_first_name, m_last_name, m_birth_date, m_city, m_phone_number, m_website)
        count = cursor.execute(query, data_tuple)

        # Сохраняем изменения
        conn.commit()
        print("Запись успешно вставлена в таблицу")

        # Выполняем запрос и получаем результат
        # query = "SELECT * FROM Users WHERE 'Birth date' = 'нет данных'"
        # count = cursor.execute(query)
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)

        # Закрываем соединение
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")

# Получаем данные от пользователя
id = input("Введите ID пользователя: ")
first_name = input("Введите имя пользователя: ")
last_name = input("Введите фамилию пользователя: ")
birth_date = input("Введите дату рождения пользователя: ")
city = input("Введите город пользователя: ")
phone_number = input("Введите номер телефона пользователя: ")
website = input("Введите сайт пользователя: ")

insert_varible_into_table(id, first_name, last_name, birth_date, city, phone_number, website)