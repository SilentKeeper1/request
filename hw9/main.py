from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        tour TEXT)''')
    conn.commit()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/book/', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    tour = request.form['tour']
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (name, email, tour) VALUES (?, ?, ?)", (name, email, tour))
        conn.commit()
    return jsonify({"message": "Бронювання успішне!"})

if __name__ == '__main__':
    app.run(port=4190, debug=True)
