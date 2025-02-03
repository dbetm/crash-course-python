from src.constants import TICKET_PATH_TEMPLATE
from src.ticket import Ticket


ticket = Ticket("David BM", 23.42, "A2")

# TICKET_PATH_TEMPLATE = "ticket_files/{timestamp}_{ticket_id}.pdf"
ticket_filepath = TICKET_PATH_TEMPLATE.format(
    timestamp=ticket.timestamp.replace(":", "_"), ticket_id=ticket.id,
)

ticket.to_pdf(ticket_filepath)