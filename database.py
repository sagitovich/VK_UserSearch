# Открываем файл для чтения
with open("database.txt", "r") as file:
    # Читаем все строки из файла и сохраняем уникальные имена в множество
    users = set(file.read().splitlines())

# Выводим имена пользователей на экран
for user in users:
    print(user)

# Открываем файл для записи
with open("database.txt", "a") as file:
    # Запрашиваем у пользователя новое имя и добавляем его в множество
    new_user = input("Введите новое имя пользователя: ")
    users.add(new_user)

    # Записываем все уникальные имена пользователей из множества в файл
    file.seek(0)
    file.truncate()
    for user in users:
        file.write(user + "\n")