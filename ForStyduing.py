import requests

s = requests.Session()
r = s.get('https://httpbin.org/')
print(r.text)