import psycopg2
from psycopg2 import OperationalError
from main import return_list
from auth import pages


def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database='NEW_KS',
            user='postgres',
            password='',
            host='',
            port=''
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_order_list_table = """
        CREATE TABLE IF NOT EXISTS public.tel_order
        ( 
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ), 
            order_date date NOT NULL, 
            order_num character varying(50) COLLATE pg_catalog."default" NOT NULL DEFAULT 'xxx'::character varying,
            detail_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
            quantity integer NOT NULL,
            price integer NOT NULL DEFAULT 0,
            links character varying COLLATE pg_catalog."default",
            order_status character varying COLLATE pg_catalog."default",
            CONSTRAINT tel_order_pkey PRIMARY KEY (id)
        )"""

con = create_connection()
execute_query(con, create_order_list_table)

insert_orders = """INSERT INTO tel_order (order_num, order_date, detail_name, quantity, price, links, order_status ) VALUES ('%s','%s','%s',%s,%s,'%s','%s')"""
for count, value in enumerate(return_list(pages)):
    if value:
        sql_q = (insert_orders % value) + ";"
        # print(sql_q)
        con.autocommit = True
        cursor = con.cursor()
        cursor.execute(sql_q)


