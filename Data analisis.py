# -*- coding: utf8 -*-
import sqlite3


id = input("ID: ")

f_name = "Liza"
l_name = "Murushkina"
sex = 'женский'
b_date = "11.09.2004"
city = 'нет данных'
ph_num = 'нет данных'
website = 'нет данных'


try:
        # Подключаемся к БД
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Выполняем запрос и получаем ИМЯ пользователя
        query_1 = "SELECT [Firstname] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        # Если имеющиеся данные не совпадают с новыми, то заменяем
        if result[0] != f_name:
                query_2 = "UPDATE Users SET [Firstname]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (f_name, id))
                conn.commit()

        # Аналогично
        # ФАМИЛИЯ пользователя
        query_1 = "SELECT [Lastname] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        if result[0] != l_name:
                query_2 = "UPDATE Users SET [Lastname]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (l_name, id))
                conn.commit()

        # ПОЛ пользователя
        query_1 = "SELECT [Sex] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        if result[0] != sex:
                query_2 = "UPDATE Users SET [Sex]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (sex, id))
                conn.commit()


        # ДР пользователя
        query_1 = "SELECT [Birth date] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        if result[0] != str(b_date):
                query_2 = "UPDATE Users SET [Birth date]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (b_date, id))
                conn.commit()

        # ГОРОД пользователя
        query_1 = "SELECT [City] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        if result[0] != city:
                query_2 = "UPDATE Users SET [City]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (city, id))
                conn.commit()

        # НОМЕР ТЕЛЕФОНА пользователя
        query_1 = "SELECT [Phone number] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        if result[0] != str(ph_num):
                query_2 = "UPDATE Users SET [Phone number]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (str(ph_num), id))
                conn.commit()

        # САЙТ пользователя
        query_1 = "SELECT [Website] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (id,))
        result = cursor.fetchone()

        if result[0] != str(website):
                query_2 = "UPDATE Users SET [Website]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (str(website), id))
                conn.commit()

        # Закрываем соединение
        cursor.close()
except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
finally:
        if conn:
            conn.close()