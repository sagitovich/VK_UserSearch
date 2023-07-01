
def info_analisis(conn, cursor, user_id, f_name, l_name, sex, b_date, city, mobile, site):
        # Выполняем запрос и получаем ИМЯ пользователя
        query_1 = "SELECT [Firstname] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        # Если имеющиеся данные не совпадают с новыми, то заменяем
        if result[0] != f_name:
                query_2 = "UPDATE Users SET [Firstname]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (f_name, user_id))
                conn.commit()


        # ФАМИЛИЯ пользователя
        query_1 = "SELECT [Lastname] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        if result[0] != l_name:
                query_2 = "UPDATE Users SET [Lastname]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (l_name, user_id))
                conn.commit()


        # ПОЛ пользователя
        query_1 = "SELECT [Sex] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        if result[0] != sex:
                query_2 = "UPDATE Users SET [Sex]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (sex, user_id))
                conn.commit()


        # ДР пользователя
        query_1 = "SELECT [Birth date] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        if result[0] != str(b_date):
                query_2 = "UPDATE Users SET [Birth date]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (b_date, user_id))
                conn.commit()


        # ГОРОД пользователя
        query_1 = "SELECT [City] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        if result[0] != city:
                query_2 = "UPDATE Users SET [City]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (city, user_id))
                conn.commit()


        # НОМЕР ТЕЛЕФОНА пользователя
        query_1 = "SELECT [Phone number] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        if result[0] != str(mobile):
                query_2 = "UPDATE Users SET [Phone number]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (str(mobile), user_id))
                conn.commit()


        # САЙТ пользователя
        query_1 = "SELECT [Website] FROM Users WHERE [VK ID]=?"
        cursor.execute(query_1, (user_id,))
        result = cursor.fetchone()

        if result[0] != str(site):
                query_2 = "UPDATE Users SET [Website]=? WHERE [VK ID]=?"
                cursor.execute(query_2, (str(site), user_id))
                conn.commit()



