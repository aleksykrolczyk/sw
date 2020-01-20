import random
import string
from datetime import datetime

PARKING_PLACES = set(range(100))


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_license():
    return ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(6)])


def get_random_car(cur, left=None):
    cur.execute("SELECT place_id FROM CARS WHERE LEFT IS NULL")
    taken = cur.fetchall()
    place_id = random.choice(tuple(PARKING_PLACES - set([x['place_id'] for x in taken])))

    data = {
        'parked': datetime.now().replace(microsecond=0),
        'left': left,
        'license': get_license(),
        'place_id': place_id,
    }

    return data