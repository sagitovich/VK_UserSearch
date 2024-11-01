# -*- coding: utf8 -*-
import sqlite3
import requests
import Data_analisis

def vk_api_user(domain):

    output_info = ''

    token = "ad96b9c4ad96b9c4ad96b9c492ae8278d7aad96ad96b9c4c90bfd7846231f51c7fc965e"
    version = 5.131
    fields = 'bdate, city, domain, contacts, site, sex'    # имя, фамилия, дата рождения, город, номер телефона, сайт, пол

    # https://api.vk.com/method/users.get?user_ids=a.sagitovich&fields=bdate&access_token=ad96b9c4ad96b9c4ad96b9c492ae8278d7aad96ad96b9c4c90bfd7846231f51c7fc965e&v=5.131

    src = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'user_ids': domain,
                                'fields': fields,
                                'access_token': token,
                                'v': version
                            }
                            )

    data = src.json()


    try:
        # ПОДКЛЮЧАЕМСЯ К БАЗЕ ДАННЫХ
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()


        if (data['response'].__len__() != 0) and (data['response'][0]['sex'] != 0):   # ЕСЛИ АККАУНТ СУЩЕСТВУЕТ

            ################ ID ИМЯ ФАМИЛИЯ ######################

            user_id = str(data['response'][0]['id'])
            f_name = data['response'][0]['first_name']
            l_name = data['response'][0]['last_name']

            output_info += ('Страница ВК: ' + 'https://vk.com/id' + user_id + '\n')
            output_info += ('Имя: ' + f_name + '\n')
            output_info += ('Фамилия: ' + l_name + '\n')

            ################ ДАТА РОЖДЕНИЯ ######################

            try:
                if data['response'][0]['bdate'] != '':
                    b_date = data['response'][0]['bdate']
                else:
                    b_date = 'нет данных'
            except:
                b_date = 'нет данных'
            output_info += ('День рождения: ' + b_date + '\n')

            ###################### ПОЛ #########################

            try:
                if data['response'][0]['sex'] != '':
                    if data['response'][0]['sex'] == 1:
                        sex = 'женский'
                    if data['response'][0]['sex'] == 2:
                        sex = 'мужской'
                    if data['response'][0]['sex'] == 0:
                        sex = 'нет данных'
                else:
                    sex = 'нет данных'
            except:
                sex = 'нет данных'
            output_info += ('Пол: ' + sex + '\n')

            #################### ГОРОД #########################

            try:
                if data['response'][0]['city']['title'] != '':
                    city = data['response'][0]['city']['title']
                else:
                    city = 'нет данных'
            except:
                city = 'нет данных'
            output_info += ('Город: ' + city + '\n')

            #################### НОМЕР ТЕЛЕФОНА #######################

            try:
                if data['response'][0]['mobile_phone'] != '':
                    mobile = data['response'][0]['mobile_phone']
                else:
                    mobile = 'нет данных'
            except:
                mobile = 'нет данных'
            output_info += ('Номер телефона: ' + mobile + '\n')

            #################### САЙТ #######################

            try:
                if data['response'][0]['site'] != '':
                    site = data['response'][0]['site']
                else:
                    site = 'нет данных'
            except:
                site = 'нет данных'
            output_info += ('Сайт: ' + site)

            #######################################################

            cursor.execute("SELECT * FROM Users WHERE [VK ID] = ?", (user_id,))  # ПРОВЕРЯЕМ ЕСТЬ ЛИ ID В БАЗЕ ДАННЫХ
            result = cursor.fetchone()

            if result:
                from Data_analisis import info_analisis
                info_analisis(conn, cursor, user_id, f_name, l_name, sex, b_date, city, mobile, site)

            else:
                # СОЗДАЁМ ЗАПРОС
                query = """INSERT INTO Users ('VK ID', Firstname, Lastname, Sex, 'Birth date', City, 'Phone number', Website) \
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

                # ВСТАВЛЯЕМ ДАННЫЕ В ТАБЛИЦУ
                data_tuple = (user_id, f_name, l_name, sex, b_date, city, mobile, site)
                count = cursor.execute(query, data_tuple)

                conn.commit()   # СОХРАНЯЕМ ИЗМЕНЕНИЯ

        else:
            output_info += 'Пользователя не существует'

        # ЗАКРЫВАЕМ СОЕДИНЕНИЕ
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()


    return output_info

