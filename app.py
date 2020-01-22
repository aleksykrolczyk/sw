import sqlite3
from .utils import dict_factory, get_random_car
from flask import Flask, render_template, jsonify, redirect, url_for, request
from datetime import datetime

DB_FILE = 'cars.db'

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


@app.route('/parked', methods=['GET'])
def get_parked():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("SELECT * FROM cars WHERE left IS NULL")
        parked = cur.fetchall()
        no_parked = len(parked)
        return jsonify(no_parked=no_parked, parked=parked)


@app.route('/parked/create', methods=['GET'])
def create_parked():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        data = get_random_car(cur)

        cur.execute("""INSERT INTO CARS(parked, left, license, place_id)
                        VALUES(?, ?, ?, ?)""", tuple(data.values()))

        return jsonify(data)


@app.route('/parked/delete/<string:license_plate>', methods=['GET'])
def delete_parked(license_plate):
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        left = datetime.now().replace(microsecond=0)
        cur.execute("""UPDATE CARS SET left=? WHERE license=?""", (left, license_plate))

        return jsonify({'status': 'ok'})


@app.route('/desktop/parked', methods=['POST'])
def create_parked_desktop():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        data = get_random_car(cur)

        cur.execute("""INSERT INTO CARS(parked, left, license, place_id)
                        VALUES(?, ?, ?, ?)""", tuple(data.values()))

        return redirect(url_for('homepage'))


@app.route('/reset', methods=['GET'])
def reset():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("DELETE FROM cars")
        return redirect(url_for('homepage'))

