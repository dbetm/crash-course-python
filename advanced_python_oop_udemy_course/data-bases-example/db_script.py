import sqlite3
from pprint import pprint
from typing import Any


DB_NAME = "cinema.db"


def create_table(query, db_name: str):
    connection = sqlite3.connect(db_name)
    connection.execute(query)

    connection.commit()
    connection.close()


# create_table(
#     query="""
# 	CREATE TABLE "seat" (
# 		"seat_id"	TEXT NOT NULL,
# 		"taken"	INTEGER,
# 		"price"	REAL,
# 		PRIMARY KEY("seat_id")
# 	);
# 	""",
#     db_name=DB_NAME
# )


def insert_record(db_name: str, table_name: str, values: dict):
	connection = sqlite3.connect(db_name)
	sql_statements = (
        f'INSERT INTO "{table_name}" {tuple(values.keys())} VALUES {tuple(values.values())}'
	)

	connection.execute(sql_statements)
	connection.commit()
	connection.close()


records = [
    {"seat_id": "A2", "taken": 0, "price": 100.0},
    {"seat_id": "A3", "taken": 1, "price": 90.0},
    {"seat_id": "A4", "taken": 0, "price": 190.0},
]

# for record in records:
# 	insert_record(DB_NAME, "seat", record)


def select_all(db_name: str, table_name: str) -> list:
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(f'SELECT * FROM "{table_name}";')
	result = cursor.fetchall()
	connection.close()
	return result

# pprint(select_all(DB_NAME, "seat"))


def select_by_id(db_name: str, table_name: str, id_name: str, id: Any):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(f'SELECT * FROM "{table_name}" WHERE "{id_name}"=?;', [id])
	result = cursor.fetchone()
	connection.close()
	return result


def update_value(db_name: str, table_name: str, id_name: str, id: Any, col_name: str, value: Any):
	connection = sqlite3.connect(db_name)
	sql_statements = (f'UPDATE "{table_name}" SET "{col_name}"=? WHERE "{id_name}"=?;')

	connection.execute(sql_statements, [value, id])
	connection.commit()
	connection.close()


def delete_record(db_name: str, table_name: str, id_name: str, id: Any):
	connection = sqlite3.connect(db_name)
	sql_statements = (f'DELETE FROM "{table_name}" WHERE "{id_name}"=?;')

	connection.execute(sql_statements, [id])
	connection.commit()
	connection.close()


update_value(DB_NAME, "seat", "seat_id", "A3", col_name="taken", value=0)
print(select_by_id(DB_NAME, "seat", "seat_id", "A3"))