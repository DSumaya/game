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


def insert_stores(connection, stores):
    try:
        sql = '''INSERT INTO stores (store_title)
                 VALUES (?)'''
        cursor = connection.cursor()
        cursor.executemany(sql, stores)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_STORES FUNCTION')


def insert_categories(connection, categories):
    try:
        sql = '''INSERT INTO categories (categories_title)
                 VALUES (?)'''
        cursor = connection.cursor()
        cursor.executemany(sql, categories)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_CATEGORIES FUNCTION')


def insert_products(connection, products):
    try:
        sql = '''INSERT INTO products (product_title, category_code, unit_price, stock_quantity, store_id)
                 VALUES (?, ?, ?, ?, ?)'''
        cursor = connection.cursor()
        cursor.executemany(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_PRODUCTS FUNCTION')


def get_stores(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT store_id, store_title FROM stores''')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching stores: {e}")
        return []


def get_products(connection, store_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT products.product_title, products.category_code, products.unit_price, products.stock_quantity, products.store_id
            FROM products
            JOIN stores ON stores.store_id = products.store_id
            WHERE products.store_id = ?
        ''', (store_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching products: {e}")
        return []


def main():
    database = 'shop.db'
    connection = create_connection(database)
    if connection:
        print('Successfully connected to database')

        sql_create_table_categories = '''CREATE TABLE IF NOT EXISTS categories (
            code INTEGER PRIMARY KEY AUTOINCREMENT,
            categories_title VARCHAR(150)
        )'''
        create_tables(connection, sql_create_table_categories)

        sql_create_table_stores = '''CREATE TABLE IF NOT EXISTS stores (
            store_id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_title VARCHAR(100)
        )'''
        create_tables(connection, sql_create_table_stores)

        sql_create_table_products = '''CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title VARCHAR(250),
            category_code INTEGER NOT NULL,
            unit_price REAL NOT NULL DEFAULT 0.0,
            stock_quantity INTEGER NOT NULL DEFAULT 0,
            store_id INTEGER NOT NULL,
            FOREIGN KEY (category_code) REFERENCES categories (code),
            FOREIGN KEY (store_id) REFERENCES stores (store_id)
        )'''
        create_tables(connection, sql_create_table_products)

        insert_categories(connection, [('Food products',), ('Electronics',), ('Clothes',)])
        insert_stores(connection, [('Asia',), ('Dordoi Plaza',), ('Apple Store',)])
        insert_products(connection, [
            ('Soda', 1, 75.6, 50, 1),
            ('Cereal', 1, 89.9, 23, 1),
            ('Milk', 1, 69.9, 20, 1),
            ('Phone', 2, 1200.0, 9, 3),
            ('Computer', 2, 1050.0, 8, 3),
            ('T-shirt', 3, 1500.9, 9, 2),
            ('Skirt', 3, 2500.9, 87, 2),
            ('Boots', 3, 2590.9, 10, 2)
        ])

        stores = get_stores(connection)
        if stores:
            print('Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:')
            for store in stores:
                print(f'{store[0]} : {store[1]}')

        while True:
            try:
                store_id = int(input('Введите id магазина: '))
                if store_id == 0:
                    print('Выход из программы')
                    break
                if any(store[0] == store_id for store in stores):
                    products = get_products(connection, store_id)
                    if products:
                        print('\nСписок продуктов в выбранном магазине: \n')
                        for product in products:
                            print(f"{product[0]} - {product[1]} - {product[2]} units")
                    else:
                        print('Продукты не найдены')
                else:
                    print('Некорректный ввод')
            except ValueError:
                print('Введите корректное значение!')
        connection.close()


if __name__ == '__main__':
    main()