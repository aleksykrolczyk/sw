import random
import string

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_license():
    return ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(6)])
