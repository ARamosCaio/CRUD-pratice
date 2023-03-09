import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "batatinha23",
    database = "teste"
)

cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"

data = (
    'Cristóvão',
    'cristovao@gmail.com',
    2
)

cursor.execute(sql, data)
connection.commit()

records_affected = cursor.rowcount

cursor.close()
connection.close()

print(records_affected, "registros alterados")