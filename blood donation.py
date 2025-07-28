import Flask
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create tables on startup (SQLite for simplicity)
def init_db():
    conn = sqlite3.connect('blood_donation.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS donors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT, age INTEGER, bloodgroup TEXT,
                    contact TEXT, last_donation TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS recipients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT, age INTEGER, bloodgroup TEXT,
                    contact TEXT, blood_required INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_donor', methods=['POST'])
def register_donor():
    name = request.form['name']
    age = request.form['age']
    bloodgroup = request.form['bloodgroup']
    contact = request.form['contact']
    last_donation = request.form['lastdonation']

    conn = sqlite3.connect('blood_donation.db')
    c = conn.cursor()
    c.execute("INSERT INTO donors (name, age, bloodgroup, contact, last_donation) VALUES (?, ?, ?, ?, ?)",
              (name, age, bloodgroup, contact, last_donation))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/register_recipient', methods=['POST'])
def register_recipient():
    name = request.form['name']
    age = request.form['age']
    bloodgroup = request.form['bloodgroup']
    contact = request.form['contact']
    required = request.form['required']

    conn = sqlite3.connect('blood_donation.db')
    c = conn.cursor()
    c.execute("INSERT INTO recipients (name, age, bloodgroup, contact, blood_required) VALUES (?, ?, ?, ?, ?)",
              (name, age, bloodgroup, contact, required))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
