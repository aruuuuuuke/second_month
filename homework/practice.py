import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION function')
    return connection

def select_all_stores(connection):
    try:
        sql = "SELECT store_id, title FROM store"
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL_STORES function')

def select_products_by_store_id(connection, store_id):
    try:
        sql = """
            SELECT p.title, c.title AS category, p.unit_price AS price, p.stock_quantity AS quantity
            FROM products p
            JOIN categories c ON p.category_code = c.code
            WHERE p.store_id = ?
        """
        cursor = connection.cursor()
        cursor.execute(sql, (store_id,))
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as error:
        print(f'{error} in SELECT_PRODUCTS_BY_STORE_ID function')



connection = create_connection('Practice')

if connection:
    while True:
        print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        stores = select_all_stores(connection)
        if not stores:
            print("Список магазинов пуст.")
            break
        for store in stores:
            print(f"{store[0]}. {store[1]}")
        user_input = input("Введите id магазина: ")
        if user_input == "0":
            print("Выход из программы.")
            break
        try:
            store_id = int(user_input)
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue
        products = select_products_by_store_id(connection, store_id)
        if products:
            for row in products:
                print(f"Название продукта: {row[0]}")
                print(f"Категория: {row[1]}")
                print(f"Цена: {row[2]}")
                print(f"Количество на складе: {row[3]}")
                print('-' * 30)
        else:
            print(f"В магазине с id {store_id} нет доступных продуктов.")

    connection.close()
else:
    print("Не удалось подключиться к базе данных.")

