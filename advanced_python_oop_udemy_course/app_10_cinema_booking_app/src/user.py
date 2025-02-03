"""
A user can book a cinema seat
if the seat is free and if the user has balance in their card.

User:
    name
    buy(seat, card)
"""
from src.card import Card
from src.seat import Seat



class User:
    def __init__(self, name: str):
        self.name = name

    def book(self, card: Card, seat: Seat, cvc: str, holder: str) -> tuple:
        charge = seat.price
        card_val_results = card.validate(cvc, holder, charge)

        if not card_val_results["is_valid"]:
            return False, card_val_results["reason"]

        if not seat.is_free():
            return False, "Seat occupied"

        card.charge(charge)
        seat.occupy()

        return True, "done"
