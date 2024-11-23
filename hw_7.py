# import sqlite3
#
# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as error:
#         print(f'{error} in CREATE_CONNECTION FUNCTION')
#     return connection
#
#
# def create_table(connection, sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql)
#     except sqlite3.Error as error:
#         print(f'{error} in CREATE_TABLE FUNCTION')
#
# def insert_products(connection, product):
#     try:
#         sql = '''INSERT INTO products (product_title, price, quantity)
#          VALUES (?, ?, ?)'''
#         cursor = connection.cursor()
#         cursor.execute(sql, product)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in INSERT_PRODUCTS FUNCTION')
#
#
# def update_quantity(connection, product):
#     try:
#         sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
#         cursor = connection.cursor()
#         cursor.execute(sql, product)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in UPDATE_QUANTITY FUNCTION')
#
#
# def update_price(connection, product):
#     try:
#         sql = '''UPDATE products SET price = ? WHERE id = ?'''
#         cursor = connection.cursor()
#         cursor.execute(sql, product)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in UPDATE_PRICE FUNCTION')
#
#
# def delete_products(connection, id):
#     try:
#         sql = '''DELETE FROM products WHERE id = ?'''
#         cursor = connection.cursor()
#         cursor.execute(sql, (id,))
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in DELETE_PRODUCTS FUNCTION')
#
#
# def select_all(connection):
#     try:
#         sql = '''SELECT * FROM products'''
#         cursor = connection.cursor()
#         cursor.execute(sql)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as error:
#         print(f'{error} in SELECT_ALL FUNCTION')
#
#
# def select_price_quantity(connection, limit):
#     try:
#         sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
#         cursor = connection.cursor()
#         cursor.execute(sql, limit)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as error:
#         print(f'{error} in SELECT_PRICE_QUANTITY FUNCTION')
#
# def select_by_name(connection):
#     try:
#         sql = '''SELECT * FROM products WHERE product_title LIKE '%Apple%' '''
#         cursor = connection.cursor()
#         cursor.execute(sql)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as error:
#         print(f'{error} in SELECT_BY_NAME FUNCTION')
#
#
# sql_to_create_products_table = '''
# CREATE TABLE products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_title VARCHAR(200) NOT NULL,
#     price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
#     quantity INTEGER NOT NULL DEFAULT 0
# )
# '''
#
# my_connection = create_connection('hw.db')
# if my_connection:
#     print('Successfully connected to database')
#     create_table(my_connection, sql_to_create_products_table)
#     insert_products(my_connection, ('Red Apple', 75.3, 10))
#     insert_products(my_connection, ('Banana', 55.8, 8))
#     insert_products(my_connection, ('Mango', 200.5, 2))
#     insert_products(my_connection, ('Soda', 150.5, 3))
#     insert_products(my_connection, ('Oil', 350.7, 1))
#     insert_products(my_connection, ('Sugar', 90.8, 3))
#     insert_products(my_connection, ('Yellow Apple', 70.2, 1))
#     insert_products(my_connection, ('Bread', 50.7, 1))
#     insert_products(my_connection, ('Cereal', 110.5, 3))
#     insert_products(my_connection, ('Meat', 500.7, 3))
#     insert_products(my_connection, ('Better', 350.8, 1))
#     insert_products(my_connection, ('Eggs', 10.5, 10))
#     insert_products(my_connection, ('Green Apple', 70.8, 1))
#     update_quantity(my_connection, (18, 13))
#     update_price(my_connection, (89, 7))
#     delete_products(my_connection, 4)
#     select_all(my_connection)
#     select_price_quantity(my_connection, (70, 7))
#     select_by_name(my_connection)
#
#
