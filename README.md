# greenParsing
Модуль создан для парсинга собственных заказов и анализа выполненных заказов из личного кабинета
После установки на сервер вносим учетные данные для входа на сайт и для подключения к БД

Добавить:
парсинг каталога товаров с ценами и записывать новые записи с изменением цены и временными метками


### FOR MAC psycopg2

if you want to use the latest installed version of Postgres:

**export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"**

and then:

**pip install psycopg2**

### FOR Linux install psycopg2

Python 3

**sudo apt install libpq-dev python3-dev**

Additional
If none of the above solve your issue, try

**sudo apt install build-essential**

or

**sudo apt install postgresql-server-dev-all**

With pip
Install the psycopg2-binary PyPI package instead, it has Python wheels for Linux and Mac OS.

**pip install psycopg2-binary**
