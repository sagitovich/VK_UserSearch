import requests
from bs4 import BeautifulSoup

user_id = input("Введите id пользователя: ")
url = "https://vk.com/" + user_id              # создание ссылки
req = requests.get(url)                        # получаем html код страницы пользователя
src = req.text                                 # переводим его в сплошной текст

with open("index.html", "w") as file:           # открываем файл "index.html" для записи (он автоматически создаётся)
    file.write(src)                             # записываем в него html код страницы пользователя

with open("index.html") as file:                # открываем файл "index.html"
    src = file.read()                           # считываем его в переменную src

soup = BeautifulSoup(src, "lxml")              # создаём переменную, вызывая которую, можно собирать данные с файла

user_name = soup.find(class_="op_header")       # получаем имя пользователя (получим список)
for i in user_name:                            # пройдёмся по каждому объекту полученного списка
    name = i.text                              # избавимся от технических символов
    print("Имя пользователя: ", f"{name.strip()}")

last_activity = soup.find(class_="pp_last_activity_text")       # получаем последнюю активность пользователя
for i in last_activity:
    activity = i.text
    print('Последняя активность: ', f"{activity.strip()}")

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
except NameError:
    print("Страница пользователя является закрытой")

print("Ссылка на страницу: ", f"{url}")        # ССЫЛКА НА СТРАНИЦУ


# user_birthday = soup.find(class_="")                            # ДАТА РОЖДЕНИЯ
# for i in user_birthday:
#     birthday = i.text
#     print("Дата рождения: ", f"{birthday.strip()}")
