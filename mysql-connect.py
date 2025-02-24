import mysql.connector

connection = mysql.connector.connect(user='Olo', password='Testowe1', host='127.0.0.1',
                                     database='webapp', auth_plugin='mysql_native_password')

query ='SELECT id, username, city FROM users'
cursor = connection.cursor()
cursor.execute(query)

for row in cursor:
    print(row)