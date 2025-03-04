import mysql.connector
from flask import Flask, request, render_template, redirect, url_for

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

#Dodawanie nowych danych 
@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'POST':
        # Pobierz dane z formularza
        nazwa = request.form['nazwa']
        miasto = request.form['miasto']
        stan_cyw = request.form['stan_cyw']

        try:
            # Nawiązanie połączenia z bazą danych
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Wykonanie zapytania SQL (dostosuj do swojej tabeli)
            query = "INSERT INTO twoja_tabela (username, city, meritalst) VALUES (%s, %s, %s)"
            cursor.execute(query, (nazwa, miasto, stan_cyw))

            # Zatwierdzenie zmian
            conn.commit()

            # Zamknięcie połączenia
            cursor.close()
            conn.close()

            # Przekierowanie na stronę główną
            return redirect(url_for('index'))

        except mysql.connector.Error as err:
            return f"Błąd podczas dodawania danych: {err}"

    # Jeśli metoda to GET, wyświetl formularz
    return render_template('dodaj.html')



#Wyświetlenie akualnej listy osób z bazy
#query ='SELECT id, username, city FROM users'
#cursor = connection.cursor()
#cursor.execute(query)

#for row in cursor:
  #  print(row)

if __name__ == '__main__':
    app.run(debug=True)