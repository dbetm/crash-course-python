"""
Card:
    database
    type
    number
    cvc
    holder
    validate(price, cvc, holder)
"""
import sqlite3

from src.constants import (
    CARD_TYPES, DEFAULT_CARD_REJECTION_REASON, INSUFFICIENT_FUNDS_MSG
)


class Card:
    table = "Card"

    def __init__(self, db_connection: sqlite3.Connection, card_type: str, card_number: str):
        self.card_type = card_type
        self.card_number = card_number
        self.db_connection = db_connection

        self.__load_extra_card_data()

    def __load_extra_card_data(self):
        assert self.card_type in CARD_TYPES, f"Given {self.card_type} is not allowed"

        cursor = self.db_connection.cursor()

        cursor.execute(
            f'SELECT cvc, holder, balance FROM {self.table} WHERE "number"=? AND "type"=?;',
            [self.card_number, self.card_type]
        )

        result = cursor.fetchone()

        if result:
            self.cvc, self.holder, self.balance = result
        else:
            raise Exception("Given card number and type was not found!!!")

    def validate(self, cvc: str, holder: str, charge: float) -> dict:
        if cvc != self.cvc or holder != self.holder:
            return {
                "is_valid": False, "reason": DEFAULT_CARD_REJECTION_REASON,
            }

        if charge > self.balance:
            return {
                "is_valid": False, "reason": INSUFFICIENT_FUNDS_MSG
            }

        return {
            "is_valid": True, "reason": None
        }

    def charge(self, charge: float):
        assert self.balance >= charge, INSUFFICIENT_FUNDS_MSG

        self.balance = self.balance - charge

        self.db_connection.execute(
            f'UPDATE {self.table} SET balance={self.balance} WHERE "number"=? AND "type"=?;',
            [self.card_number, self.card_type]
        )
        self.db_connection.commit()