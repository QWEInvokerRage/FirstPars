import requests
from bs4 import BeautifulSoup
import fake_useragent

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0', 'accept': '*/*'}
session = requests.Session()
print("Введите данные для авторизации на сайте.")
def datasGen():
    data = {
        'username': None,
            'password': None,
            'loginbtn': None
    }

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
# datas = {
#     'username': 'kpobegaylo@mail.ru',
#     'password': '632',
#     'loginbtn': 'Вход'
# }
data = {
    'username': None,
    'password': None,
    'loginbtn': None
}

def datasGen():
    for key in data:
        data[key]=input("Введите" + key)

autorize = 'https://portfolio.rsue.ru/login/index.php'

responce = session.post(autorize, data=datas, headers=header).text
# print(responce)

profile_page = "https://portfolio.rsue.ru/portfolio/index.php?section=23"
profile_responce = session.get(profile_page).text
# print(profile_responce)


soup = BeautifulSoup(profile_responce, 'html.parser')
# print(soup.prettify())
# subjects = soup.find_all(class_="simpletable")

with open('resultWR.txt', 'w', encoding="utf-8") as file:
  file.write(soup.prettify())
