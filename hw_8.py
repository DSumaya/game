import sqlite3


def create_connection(db_name):
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(e)


def create_tables(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(f'{e} in CREATE_TABLE FUNCTION')


def insert_countries(connection, countries):
    try:
        sql = '''INSERT INTO countries (country_title)
                 VALUES (?)'''
        cursor = connection.cursor()
        cursor.executemany(sql, countries)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_COUNTRIES FUNCTION')


def insert_cities(connection, cities):
    try:
        sql = '''INSERT INTO cities (city_title, city_area, country_id)
                 VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.executemany(sql, cities)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_CITIES FUNCTION')


def insert_students(connection, students):
    try:
        sql = '''INSERT INTO students (first_name, last_name, city_id)
                 VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.executemany(sql, students)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_STUDENTS FUNCTION')


def get_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT city_id, city_title FROM cities''')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f'{e}')
        return []


def get_students(connection, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT students.first_name, students.last_name, cities.city_title
            FROM students
            JOIN cities ON students.city_id = cities.city_id
            WHERE cities.city_id = ?
        ''', (city_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching students: {e}")
        return []


def main():
    database = 'hw_8.db'
    connection = create_connection(database)
    if connection:
        print('Successfully connected to database')

        sql_create_table_countries = '''CREATE TABLE IF NOT EXISTS countries(
            country_id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_title TEXT NOT NULL
        )'''
        create_tables(connection, sql_create_table_countries)

        sql_create_table_cities = '''CREATE TABLE IF NOT EXISTS cities (
            city_id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_title TEXT NOT NULL,
            city_area REAL NOT NULL,
            country_id INTEGER NOT NULL,
            FOREIGN KEY (country_id) REFERENCES countries (country_id)
        )'''
        create_tables(connection, sql_create_table_cities)

        sql_create_table_students = '''CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city_id INTEGER NOT NULL,
            FOREIGN KEY (city_id) REFERENCES cities (city_id)
        )'''
        create_tables(connection, sql_create_table_students)

        # Insert data
        insert_countries(connection, [('Kyrgyzstan',), ('Turkey',), ('Italy',)])
        insert_cities(connection, [
            ('Bishkek', 120, 1),
            ('Tokmok', 50, 1),
            ('Osh', 55, 1),
            ('Istanbul', 500, 2),
            ('Ankara', 4500, 2),
            ('Rome', 890, 3),
            ('Milan', 560, 3)
        ])
        insert_students(connection, [
            ('Alexander', 'Smith', 1),
            ('Maria', 'Johnson', 2),
            ('Dmitry', 'Brown', 3),
            ('Anna', 'Williams', 4),
            ('Sergey', 'Jones', 5),
            ('Elena', 'Garcia', 6),
            ('Nikolai', 'Miller', 7),
            ('Olga', 'Davis', 1),
            ('Andrew', 'Wilson', 2),
            ('Victoria', 'Martinez', 3),
            ('Paul', 'Anderson', 4),
            ('Tatiana', 'Taylor', 5),
            ('Igor', 'Thomas', 6),
            ('Natalia', 'Moore', 4),
            ('Roman', 'Jackson', 4),
        ])

        # Fetch and display cities
        cities = get_cities(connection)
        if cities:
            print('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, '
                  'для выхода из программы введите 0:')
            for city in cities:
                print(f'{city[0]} - {city[1]}')

            while True:
                try:
                    city_id = int(input('Введите id города: '))
                    if city_id == 0:
                        print('Выход из программы.')
                        break

                    elif any(city_id == city[0] for city in cities):
                        students = get_students(connection, city_id)
                        if students:
                            print('Список студентов в выбранном городе:')
                            for student in students:
                                print(f'Имя: {student[0]}, Фамилия: {student[1]}')
                        else:
                            print('Студенты не найдены.')
                    else:
                        print('Некорректный ввод.')
                except ValueError:
                    print('Введите корректное значение!')

        connection.close()


if __name__ == '__main__':
    main()