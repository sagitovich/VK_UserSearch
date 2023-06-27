import requests
from bs4 import BeautifulSoup

user_id = input("Введите id пользователя: ")
url = "https://vk.com/" + user_id              # создание ссылки
src = requests.get(url).text                   # получаем html код страницы пользователя и переводим его в сплошной текст

with open("index.html", "w") as file:           # открываем файл "index.html" для записи (он автоматически создаётся)
    file.write(src)                             # записываем в него html код страницы пользователя

with open("index.html") as file:                # открываем файл "index.html"
    src = file.read()                           # считываем его в переменную src

soup = BeautifulSoup(src, "lxml")              # создаём переменную, вызывая которую, можно собирать данные с файла

exists = True
try:
    user_name = soup.find(class_="op_header").text       # получаем имя пользователя и переводим его в текст
    print("Имя пользователя: ", f"{user_name.strip()}")
except:
    exists = False
    print("Пользователя с таким id не существует")
# суть в том, что, если пользователя не существует, то паркер не найдёт таких данных, как "имя пользователя"


if exists:                                         # если страница существует

    try:
        flag_Activity = False
        last_activity = soup.find(class_="pp_last_activity_text")       # получаем последнюю активность пользователя
        if not flag_Activity:
            flag_Activity = True
            for i in last_activity:
                activity = i.text
                print('Последняя активность: ', f"{activity.strip()}")
    except:
        print("Невозможно получить данные о последней активности пользователя")

    try:
        a = []
        cnt = 0
        about_user = soup.find_all(class_="OwnerInfo__rowCenter")    # получаем подробную информацию о пользователе
        for i in about_user:
            about = i.text
            a.append(about)
            cnt += 1
        for i in range(0, cnt - 1):
            print(f"{a[i].strip()}")
    except:
        print("Страница пользователя является закрытой")

    print("Ссылка на страницу: ", f"{url}")  # ССЫЛКА НА СТРАНИЦУ

    user_access = soup.find(class_="service_msg service_msg_null").text
    print(user_access)

else:
    exit()


# user_birthday = soup.find(class_="")                            # ДАТА РОЖДЕНИЯ
# for i in user_birthday:
#     birthday = i.text
#     print("Дата рождения: ", f"{birthday.strip()}")
