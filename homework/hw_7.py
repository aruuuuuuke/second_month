import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION function')
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        print("Table created successfully!")
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE function')



def insert_products(connection, product):
    try:
        sql = """INSERT INTO products 
        (product_title, price, quantity)
        VALUES (?, ?, ?)"""
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in INSERT_PRODUCTS function')


def update_quantity(connection, product):
    try:
        sql = """UPDATE products SET quantity = ? WHERE id = ?"""
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_QUANTITY function')

def update_price(connection, product):
    try:
        sql = """UPDATE products SET price = ? WHERE id = ?"""
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_PRICE function')

def delete_by_id(connection, id):
    try:
        sql = """DELETE FROM products WHERE id = ?"""
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in DELETE_BY_ID function')


def select_all(connection):
    try:
        sql = """SELECT * FROM products """
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL function')


def select_by_price_quantity(connection, limit):
    try:
        sql = """SELECT * FROM products 
        WHERE price <= ? AND quantity >= ? """
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_PRICE_QUANTITY function')


def select_by_name(connection):
    try:
        sql = """SELECT * FROM products 
        WHERE product_title LIKE '%milk%'"""
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_NAME function')


sql_to_cerate_products_table = """
CREATE TABLE PRODUCTS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
"""


my_connection = create_connection('hw.db')


if my_connection:
    print('Connected successfully!')
    create_table(my_connection, sql_to_cerate_products_table)
    insert_products(my_connection, ('Banana', 37.5, 6))
    insert_products(my_connection, ('Banana milk', 50, 9))
    insert_products(my_connection, ('milky ice-cream', 30, 8))
    insert_products(my_connection, ('milkyway', 70.6, 10))
    insert_products(my_connection, ('apple', 40, 30))
    insert_products(my_connection, ('peach', 60.5, 32))
    insert_products(my_connection, ('orange', 55, 22))
    insert_products(my_connection, ('cheese from milk', 115, 6))
    insert_products(my_connection, ('chery', 97, 40))
    insert_products(my_connection, ('milk', 65, 5))
    insert_products(my_connection, ('milkshake', 75, 7))
    insert_products(my_connection, ('cucumber', 50, 30))
    insert_products(my_connection, ('potato', 60, 30))
    insert_products(my_connection, ('tomate', 55.5, 22))
    update_price(my_connection, (50, 1))
    update_quantity(my_connection, (15, 11))
    delete_by_id(my_connection, 1)
    select_all(my_connection)
    select_by_price_quantity(my_connection, (50, 3))
    select_by_name(my_connection)
