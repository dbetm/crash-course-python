from __future__ import annotations
from typing import List


class Bill:
    """Create a bill that contains the amount to pay an the corresponding 
    period of time."""

    def __init__(self, amount: float, period: str):
        self.amount = amount
        self.period = period


class Flatmate:
    """Create a flatmate person who lives in the flat and pays a share of the bill."""

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house
    
    def pay(self, bill: Bill, co_flatmates: List[Flatmate]) -> float:
        days_all_flatmates = (
            self.days_in_house + sum([f.days_in_house for f in co_flatmates])
        )
        weight = self.days_in_house / days_all_flatmates

        return bill.amount * weight

    def get_co_flatmates(self, flatmates: List[Flatmate]) -> list:
        return [flatmate for flatmate in flatmates if flatmate != self]