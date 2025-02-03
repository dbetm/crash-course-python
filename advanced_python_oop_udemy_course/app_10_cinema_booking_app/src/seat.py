import sqlite3

"""
Seat:
    db_connection
    seat_id
    taken
    price
    is_free()
    occupy()
    release()
"""


class Seat:
    table = "Seat"

    def __init__(self, db_connection: sqlite3.Connection, seat_id: str):
        self.db_connection = db_connection
        self.seat_id = seat_id

        self.__get_seat_data()

    def __get_seat_data(self):
        cursor = self.db_connection.cursor()

        cursor.execute(
            f'SELECT taken, price FROM "{self.table}" WHERE "seat_id"=?;', [self.seat_id]
        )

        result = cursor.fetchone()

        if result:
            self.taken, self.price = result
        else:
            raise Exception(f"Seat was not found for {self.seat_id} seat_id")

    def is_free(self) -> bool:
        return self.taken == 0

    def occupy(self) -> None:
        self.db_connection.execute(
            f'UPDATE {self.table} SET taken=1 WHERE "seat_id"=?;', [self.seat_id]
        )
        self.db_connection.commit()

        self.taken = 1

    def release(self) -> None:
        self.db_connection.execute(
            f'UPDATE {self.table} SET taken=0 WHERE "seat_id"=?;', [self.seat_id]
        )
        self.db_connection.commit()

        self.taken = 0

    @staticmethod
    def get_available_seats(db_connection: sqlite3.Connection):
        cursor = db_connection.cursor()       
        cursor.execute(f'SELECT seat_id FROM "{Seat.table}" WHERE taken=0;')

        return cursor.fetchall()

    def __str__(self) -> str:
        return f"{self.seat_id=}, {self.taken=}, {self.price=}"