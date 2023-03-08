import mysql.connector
import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="batatinha23",
    database="teste"
)

cursor = connection.cursor()

sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"

data = (
    'Primeiro Usuário',
    'primeirousuario@teste.com.br',
    datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:", userid)