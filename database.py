import psycopg2
import os

from psycopg import connection, cursor

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="987091werf"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Успешное подключение Версия бд: {db_version}")

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Ошибка {error}")