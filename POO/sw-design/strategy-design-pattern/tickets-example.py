import random
import string
from abc import ABC, abstractmethod
from typing import List


def generate_id(length: int = 8) -> str:
    return ""


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list_: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_: List[SupportTicket]) -> List[SupportTicket]:
        return list_.copy()


class FILOOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list_.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list_.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_: List[SupportTicket]) -> List[SupportTicket]:
        return []


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
    
    # Instead of receiving a object-class it could be a callable function.
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # if it's empty, don't do anything
        if not self.tickets:
            print("There are no tickets to process. Well done!")
            return

        # create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)

        for ticket in ticket_list:
            self.process_ticket(ticket)
    
    def process_ticket(self, ticket: SupportTicket):
        print("=====================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("=====================")


# create the application
app = CustomerSupport()

# register new tickets
app.create_ticket("Jhon Smith", "My computer makes strange sounds")
app.create_ticket("Linus Hey", "I can't upload any videos, please help.")
app.create_ticket("Arjan Coding", "VSCode doesn't automatically solve my bugs.")

# process the tickets
random_strategy = RandomOrderingStrategy()
fifo_strategy = FIFOOrderingStrategy()
black_hole_strategy = BlackHoleOrderingStrategy()
app.process_tickets(black_hole_strategy)
