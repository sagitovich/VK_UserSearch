import requests
from bs4 import BeautifulSoup


def parser():

    output_info = ''    # строка на вывод собранных данных в файл
    user_id = input("Введите id пользователя: ")
    url = "https://vk.com/" + user_id # создание ссылки
    src = requests.get(url).text  # получаем html код страницы пользователя и переводим его в сплошной текст

    with open("user.html", "w") as file:  # открываем файл "index.html" для записи (он автоматически создаётся)
        file.write(src)  # записываем в него html код страницы пользователя

    with open("user.html") as file:  # открываем файл "index.html"
        src = file.read()  # считываем его в переменную src

    soup = BeautifulSoup(src, "lxml")  # создаём переменную, вызывая которую, можно собирать данные с файла

    exists = True
    try:
        user_name = soup.find(class_="op_header").text  # получаем имя пользователя и переводим его в текст
        output_info += ('Имя пользователя: ' + user_name.strip() + '\n')
    except:
        exists = False
        output_info += ('Пользователя с таким id не существует' + '\n')

        print(output_info)
        with open('data.txt', 'w') as file:
            file.write(output_info)

    if exists:  # если страница существует

        try:
            last_activity = soup.find(class_="pp_last_activity_text").text  # получаем последнюю активность пользователя
            output_info += ('Последняя активность: ' + last_activity.strip() + '\n')
        except:
            output_info += ('Невозможно получить данные о последней активности пользователя' + '\n')

        try:
            a = []
            cnt = 0
            about_user = soup.find_all(class_="OwnerInfo__rowCenter")  # получаем подробную информацию о пользователе
            for i in about_user:
                about = i.text
                a.append(about)
                cnt += 1
            for i in range(0, cnt - 1):
                output_info += (a[i].strip() + '\n')

        except:
            output_info += ('Страница пользователя является закрытой' + '\n')

        output_info += ('Ссылка на страницу: ' + url + '\n')

        # print(output_info)

        with open('data.txt', 'w') as file:
            file.write(output_info)

    else:
        exit()


parser()