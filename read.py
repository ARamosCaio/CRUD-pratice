import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="batatinha23",
    database="teste"
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print(result)