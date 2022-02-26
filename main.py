from bs4 import BeautifulSoup
import requests
from auth import pages

results = []


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def write_file(text):
    with open('export.txt', 'w') as ex_file:
        ex_file.write(text)


def find_quant(tagg, i):
    pr_items = tagg.find_all('div', {'class': 'quantity'})
    for count, value in enumerate(pr_items):
        if count == i:
            quant = value.text
    return quant


def find_price(tagg, i):
    pr_items = tagg.find_all('div', {'class': 'price'})
    for count, value in enumerate(pr_items):
        if count == i:
            price = value.text
    return price


def get_date(ddate):
    months = {"Января":"01", "Февраля":"02", "Марта":"03", "Апреля":"04", "Мая":"05","Июня":"06","Июля":"07","Августа":"08","Сентября":"09", "Октября":"10","Ноября":"11","Декабря":"12"}
    days = {"1":"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
    if ddate.split(' ')[1] in months:
        if ddate.split(' ')[0] in days:
            res = ddate.split(' ')[2] + '-' + months[ddate.split(' ')[1]] + '-' + days[ddate.split(' ')[0]]
        else:
            res = ddate.split(' ')[2] + '-' + months[ddate.split(' ')[1]] + '-' + ddate.split(' ')[0]
        return res
    else:
        return '01.01.2000'


def parse_user_datafile_bs(text):
    soup = BeautifulSoup(text, 'lxml')
    film_list = soup.find('div', {'class': 'order-list'})
    items = film_list.find_all('div', {'class': 'order-item'})
    i = 0
    for item in items:
        order_num = item.find('span', {'class': 'number'}).text.strip().replace('Заказ № ', '')
        order_status = item.find('span', {'class': 'name'}).text.strip()
        order_date = item.find('span', {'class': 'date-'}).text.strip().replace('от ', '')
        i +=1
        pr_items = item.find_all('div', {'class': 'product'})
        if order_status == 'Выполнен' or order_status == 'Подтвержден':
            for count, value in enumerate(pr_items):
                name_prod = value.text.replace('\n', '')
                link = value.find('a').get('href')
                quant = find_quant(item, count)
                price = find_price(item, count)
                results.append((order_num, get_date(order_date), name_prod, int(quant.split(' ')[0]), int(price.replace(' ', '').split('.')[0]), link.replace(' ', '%20').strip(), order_status))


def return_list(pagess):
    for page in pagess:
        results.append(parse_user_datafile_bs(page))
    return results

# return_list(pages)
# for result in results:
#     if result:
#         print(result)

