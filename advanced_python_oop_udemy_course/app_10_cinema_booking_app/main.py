import sqlite3

from src.card import Card
from src.constants import CARD_TYPES, TICKET_PATH_TEMPLATE
from src.seat import Seat
from src.ticket import Ticket
from src.user import User


cinema_db_connection = sqlite3.connect("cinema.db")
banking_db_connection = sqlite3.connect("banking.db")


# card = Card(banking_db_connection, "Visa", card_number="12345678")

# print(card.validate("123", "John Smith", 5000))

# seat = Seat(cinema_db_connection, "A3")

# print("is free", seat.is_free())
# seat.occupy()
# print(seat)
# print("is free", seat.is_free())


card_type = input(f"Card Type {CARD_TYPES}: ")
card_number = input("Card number: ")
cvc = input("CVC: ")
holder = input("Card holder: ")

available_seats = [
    result[0] for result in Seat.get_available_seats(cinema_db_connection)
]
seat_id = input(f"Seat, choose from {available_seats}: ")
client_name = input("Type your name: ")

card = Card(banking_db_connection, card_type, card_number=card_number)
seat = Seat(cinema_db_connection, seat_id)
user = User(client_name)

print(user.book(card, seat, cvc, holder))

cinema_db_connection.close()
banking_db_connection.close()

print("Generating ticket...")

ticket = Ticket(client_name, seat.price, seat.seat_id)

# TICKET_PATH_TEMPLATE = "ticket_files/{timestamp}_{ticket_id}.pdf"
ticket_filepath = TICKET_PATH_TEMPLATE.format(
    timestamp=ticket.timestamp.replace(":", "_"), ticket_id=ticket.id,
)

ticket.to_pdf(ticket_filepath)