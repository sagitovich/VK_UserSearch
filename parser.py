import requests
from bs4 import BeautifulSoup

user_id = input("Введите id пользователя: ")

url = "https://vk.com/" + user_id
req = requests.get(url)
src = req.text

with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

print("Ссылка на страницу: ", f"{url}")        # ССЫЛКА НА СТРАНИЦУ

user_name = soup.find(class_="op_header")       # ИМЯ
for i in user_name:
    name = i.text
    print("Имя пользователя: ", f"{name.strip()}")

# last_activity = soup.find(class_="pp_last_activity_text")       # ПОСЛЕДНЯЯ АКТИВНОСТЬ
# for i in last_activity:
#     activity = i.text
#     print("Последняя активность: ", f"{activity.strip()}")

# user_birthday = soup.find(class_="")                            # ДАТА РОЖДЕНИЯ
# for i in user_birthday:
#     birthday = i.text
#     print("Дата рождения: ", f"{birthday.strip()}")

try:
    a = []
    cnt = 0
    about_user = soup.find_all(class_="OwnerInfo__rowCenter")    # ПОДРОБНАЯ ИНФА
    for i in about_user:
        about = i.text
        a.append(about)
        cnt += 1
    for i in range(0, cnt - 1):
        print(f"{a[i].strip()}")
except:
    print("Страница пользователя является закрытой")
