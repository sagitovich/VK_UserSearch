import csv
import requests

domain = input("Введите id пользователя: ")
output_info = ''

token = "ad96b9c4ad96b9c4ad96b9c492ae8278d7aad96ad96b9c4c90bfd7846231f51c7fc965e"
version = 5.131
fields = 'bdate, city, domain, contacts, site'    # имя, фамилия, дата рождения, город, номер телефона, сайт
user_info = []

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
user_info.extend(data)


with open('info.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(('Имя', 'Фамилия', 'Дата рождения', 'Город', 'Номер телефона', 'Cайт'))
    write.writerow((data['response'][0]['first_name'], data['response'][0]['last_name'], data['response'][0]['bdate'], data['response'][0]['city']['title'], data['response'][0]['mobile_phone'], data['response'][0]['site']))

    output_info += ('Имя: ' + data['response'][0]['first_name'] + '\n')
    output_info += ('Фамилия: ' + data['response'][0]['last_name'] + '\n')
    output_info += ('Дата рождения: ' + data['response'][0]['bdate'] + '\n')
    output_info += ('Город: ' + data['response'][0]['city']['title'] + '\n')
    output_info += ('Номер телефона: ' + data['response'][0]['mobile_phone'] + '\n')
    output_info += ('Cайт: ' + data['response'][0]['site'])

print(output_info)

