import requests
from requests.auth import HTTPBasicAuth
from logopass import PASSWORD_SITE, LOGIN_SITE

login = LOGIN_SITE
password = PASSWORD_SITE
pages = []
s = requests.session()
headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
# s.headers.update(headers)

req = requests.get('https://green-spark.ru/personal/orders/?per_page=100', auth=HTTPBasicAuth(login, password))
pages.append(req.text)
req = requests.get('https://green-spark.ru/personal/orders/?PAGEN_1=2&per_page=100', auth=HTTPBasicAuth(login, password))
pages.append(req.text)
req = requests.get('https://green-spark.ru/personal/orders/?PAGEN_1=3&per_page=100', auth=HTTPBasicAuth(login, password))
pages.append(req.text)
req = requests.get('https://green-spark.ru/personal/orders/?PAGEN_1=4&per_page=100', auth=HTTPBasicAuth(login, password))
pages.append(req.text)
req = requests.get('https://green-spark.ru/personal/orders/?PAGEN_1=5&per_page=100', auth=HTTPBasicAuth(login, password))
pages.append(req.text)

