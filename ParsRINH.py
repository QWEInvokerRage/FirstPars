import requests
from bs4 import BeautifulSoup
import fake_useragent

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0', 'accept': '*/*'}
session = requests.Session()
user = fake_useragent.UserAgent().random
header = {'user-agent': user}

datas = {
    'username': '',
    'password': '',
    'loginbtn': ''
}


def datasGen(datas):
    print("В loginbtn введите 'Вход' ")
    for key in datas:
        datas[key] = input("Введите" + " " + key + ":")

    return datas
datasGen(datas)
# datas = datasGen(datas)

autorize = 'https://portfolio.rsue.ru/login/index.php'

responce = session.post(autorize, data=datas, headers=header).text
# print(responce)

profile_page = "https://portfolio.rsue.ru/portfolio/index.php?section=23"
profile_responce = session.get(profile_page).text


# print(profile_responce)

def soupovarka(profile_responce):
    soup = BeautifulSoup(profile_responce, 'html.parser')
    subjects = str(soup.find_all(class_="simpletable"))
    return subjects

with open('resultWR.txt', 'w', encoding="utf-8") as file:
    file.write(soupovarka(profile_responce))
# print(soupovarka())
# print(datas)