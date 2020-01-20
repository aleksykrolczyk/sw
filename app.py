import sqlite3
import random
from datetime import datetime
from .utils import get_license, dict_factory
from flask import Flask, render_template, jsonify, request

DB_FILE = 'cars.db'
PARKING_PLACES = set(range(100))

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

        cur.execute("SELECT * FROM cars WHERE left IS NOT  NULL")
        parked = cur.fetchall()
        no_parked = len(parked)
        return jsonify(no_parked=no_parked, parked=parked)


@app.route('/parked', methods=['POST'])
def create_parked():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("SELECT place_id FROM CARS WHERE LEFT IS NULL")
        taken = cur.fetchall()
        place_id = random.choice(tuple(PARKING_PLACES - set([x['place_id'] for x in taken])))

        data = {
            'parked': datetime.now().replace(microsecond=0),
            'left': None,
            'license': get_license(),
            'place_id': place_id,
        }
        cur.execute("""INSERT INTO CARS(parked, left, license, place_id)
                        VALUES(?, ?, ?, ?)""", tuple(data.values()))

        return jsonify(data)

