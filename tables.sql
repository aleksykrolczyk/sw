CREATE TABLE cars(
    id INTEGER PRIMARY KEY,
    parked DATETIME NOT NULL,
    left DATETIME,
    license TEXT,
    place_id INTEGER
);

DROP TABLE CARS;


INSERT INTO cars(parked, left, license, place_id)
    VALUES (CURRENT_TIMESTAMP, NULL , 'ABC1', 12);

INSERT INTO cars(parked, left, license, place_id)
    VALUES (CURRENT_TIMESTAMP, NULL , 'ABC2', 54);

INSERT INTO cars(parked, left, license, place_id)
    VALUES (CURRENT_TIMESTAMP, NULL , 'ABC3', 82);

INSERT INTO cars(parked, left, license, place_id)
    VALUES (CURRENT_TIMESTAMP, NULL , 'ABC4', 42);



INSERT INTO cars(parked, left, license, place_id)
    VALUES (datetime('now', '-1 hours'), CURRENT_TIMESTAMP , 'ABC5', 7);

INSERT INTO cars(parked, left, license, place_id)
    VALUES (datetime('now', '-2 hours'), CURRENT_TIMESTAMP , 'ABC6', 45);

INSERT INTO cars(parked, left, license, place_id)
    VALUES (datetime('now', '-3 hours'), CURRENT_TIMESTAMP , 'ABC7', 65);

INSERT INTO cars(parked, left, license, place_id)
    VALUES (datetime('now', '-4 hours'), CURRENT_TIMESTAMP , 'ABC8', 99);