import mysql.connector
from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

# Konfiguracja połączenia z bazą danych MS SQL
db_config = {
    'host': '127.0.0.1',
    'user': 'Olo',
    'password': 'Testowe1',
    'database': 'webapp',
    'auth_plugin':'mysql_native_password'
}


@app.route('/')
def index():
    try:
      # Nawiązanie połączenia z bazą danych
        conn = mysql.connector.connect(**db_config)
        #conn = mysql.connector.connect(user='Olo', password='Testowe1', host='127.0.0.1',
        #                               database='webapp', auth_plugin='mysql_native_password')
        cursor = conn.cursor(dictionary=True)
        # Wykonanie zapytania SQL
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        # Zamknięcie połączenia
        cursor.close()
        conn.close()

        # Przekazanie danych do szablonu HTML
        return render_template('index.html', data=data)

    except mysql.connector.Error as err:
        return f"Błąd połączenia z bazą danych: {err}"   



#Wyświetlenie akualnej listy osób z bazy
#query ='SELECT id, username, city FROM users'
#cursor = connection.cursor()
#cursor.execute(query)

#for row in cursor:
  #  print(row)


if __name__ == '__main__':
    app.run(debug=True)