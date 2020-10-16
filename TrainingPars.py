from bs4 import BeautifulSoup
import re

with open('resultWR.txt', 'r', encoding='UTF-8') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'lxml')
    root = soup.html
    for oIter in root:
        notBe = root.find_all(string=re.compile('Неявка'))
        accessDenied = root.find_all(string=re.compile('Незачет'))
        print(accessDenied, notBe)