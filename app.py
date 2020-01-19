import sqlite3
from datetime import datetime
from flask import Flask, render_template, jsonify

DB_FILE = 'cars.db'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = Flask(__name__)
app.run()

@app.route('/')
@app.route('/homepage')
def homepage():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("SELECT * FROM cars WHERE left IS NULL")
        parked = cur.fetchall()
        no_parked = len(parked)

        return render_template('main.html', parked=parked, no_parked=no_parked)

@app.route('/parked')
def get_parked():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("SELECT * FROM cars WHERE left IS NOT  NULL")
        parked = cur.fetchall()
        no_parked = len(parked)
        return jsonify(no_parked=no_parked, parked=parked)