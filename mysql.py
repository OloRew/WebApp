import mysql.connector

connection = mysql.connector.connect(user='olo',password='Olo1234',host='127.0.0.1',
                                     database='webapp', auth_plugin='mysql_native_password')

query ='SELECT id, username, city FRM users'
cursor = connection.cursor()
cursor.execute(query)

for row in cursor:
    print(row)