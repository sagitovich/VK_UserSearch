import requests
from bs4 import BeautifulSoup


def parser(user_id):
    url = "https://vk.com/" + user_id  # создание ссылки
    src = requests.get(url).text  # получаем html код страницы пользователя и переводим его в сплошной текст

    with open("user.html", "w") as file:  # открываем файл "index.html" для записи (он автоматически создаётся)
        file.write(src)  # записываем в него html код страницы пользователя

    with open("user.html") as file:  # открываем файл "index.html"
        src = file.read()  # считываем его в переменную src

    soup = BeautifulSoup(src, "lxml")  # создаём переменную, вызывая которую, можно собирать данные с файла

    exists = True
    try:
        user_name = soup.find(class_="op_header").text  # получаем имя пользователя и переводим его в текст
        third_mess_1_1 = "Имя пользователя: "
        third_mess_1_2 = f"{user_name.strip()}\n"
        third_mess_1 = third_mess_1_1 + third_mess_1_2 #Вывод фамилии имени, аналогичное принту ниже
        #print("Имя пользователя: ", f"{user_name.strip()}")
    except:
        exists = False
        third_mess_1 = "Пользователя с таким id не существует"
        return third_mess_1
        #print("Пользователя с таким id не существует")
    # суть в том, что, если пользователя не существует, то паркер не найдёт таких данных, как "имя пользователя"

    if exists:  # если страница существует

        try:
            last_activity = soup.find(class_="pp_last_activity_text").text  # получаем последнюю активность пользователя
            third_mess_2_1 = 'Последняя активность: '
            third_mess_2_2 = f"{last_activity.strip()}\n"
            third_mess_2 = third_mess_2_1 + third_mess_2_2 #Вывод последней активности, аналогичное принту ниже
            #print('Последняя активность: ', f"{last_activity.strip()}")
        except:
            third_mess_2 = "Невозможно получить данные о последней активности пользователя\n"
            #print("Невозможно получить данные о последней активности пользователя")

        try:
            a = []
            third_mess_3 = ""
            cnt = 0
            about_user = soup.find_all(class_="OwnerInfo__rowCenter")  # получаем подробную информацию о пользователе
            for i in about_user:
                about = i.text
                a.append(about)
                cnt += 1
            for i in range(0, cnt - 1):
                third_mess_3 += f"{a[i].strip()}\n"
                #print(f"{a[i].strip()}")

        except:
            third_mess_3 = "Страница пользователя является закрытой"

        third_mess_4_1 = "Ссылка на страницу: "
        third_mess_4_2 = f"{url}"
        third_mess_4 = third_mess_4_1 + third_mess_4_2  #Вывод ссылки на страницу аналогично нижнему принту (только в виде переменной)
        #print("Ссылка на страницу: ", f"{url}")  # ССЫЛКА НА СТРАНИЦУ
        third_mess = third_mess_1 + third_mess_2 + third_mess_3 + third_mess_4
        return third_mess
    else:
        exit()


#parser()

# user_birthday = soup.find(class_="")                            # ДАТА РОЖДЕНИЯ
# for i in user_birthday:
#     birthday = i.text
#     print("Дата рождения: ", f"{birthday.strip()}")
