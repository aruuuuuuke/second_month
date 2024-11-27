import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION function')
    return connection

def get_all_cities(connection):
    try:
        sql = """SELECT id, title FROM cities"""
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except sqlite3.Error as error:
        print(f'{error} in GET_ALL_CITIES function')


def get_students_by_city_id(connection, city_id):
    try:
        sql = """
            SELECT s.first_name, s.last_name, co.title AS country, c.title AS city, c.area
            FROM students as s
            JOIN cities as c ON s.city_id = c.id
            JOIN countries co ON c.country_id = co.id
            WHERE c.id = ?
        """
        cursor = connection.cursor()
        cursor.execute(sql, (city_id,))
        return cursor.fetchall()
    except sqlite3.Error as error:
        print(f'{error} in GET_STUDENTS_BY_CITY_ID function')


def main():
    db_name = 'hw8'
    connection = create_connection(db_name)
    if not connection:
        print("Не удалось подключиться к базе данных.")
        return

    print("Подключение к базе данных успешно установлено!")

    while True:
        print("\nВы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        cities = get_all_cities(connection)
        if not cities:
            print("Не удалось получить список городов.")
            break

        for city in cities:
            print(f"{city[0]}. {city[1]}")
        try:
            city_id = int(input("\nВведите id города: "))
        except ValueError:
            print("Введите корректное число.")
            continue
        if city_id == 0:
            print("Выход из программы.")
            break

        students = get_students_by_city_id(connection, city_id)
        if students:
            print(f"\nУченики из города с id {city_id}:")
            for student in students:
                print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")
        else:
            print(f"Учеников из города с id {city_id} не найдено.")
    connection.close()

if __name__ == "__main__":
    main()