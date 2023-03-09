import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "batatinha23",
    database = "teste"
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"

data = (2,)

cursor.execute(sql, data)
connection.commit()
 
records_affected = cursor.rowcount
cursor.close()
connection.close()

print(records_affected, "registros excluídos")
