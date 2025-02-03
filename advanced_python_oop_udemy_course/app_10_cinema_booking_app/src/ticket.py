"""
Ticket:
    id
    client_name
    total
    seat_id
    to_pdf(path)
"""
from datetime import datetime
from uuid import uuid4

from fpdf import FPDF



class Ticket:
    def __init__(self, client_name: str, total: float, seat_id: str):
        self.id = self.__get_ticket_id()
        self.timestamp = self.__get_timestamp()
        self.client_name = client_name
        self.total = total
        self.seat_id = seat_id

    def __get_ticket_id(self) -> str:
        return str(uuid4())
    
    def __get_timestamp(self) -> str:
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def to_pdf(self, filepath: str) -> None:
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Digital Ticket", border=1, align="C", ln=1)

        # Change font
        pdf.set_font(family="Times", size=14, style="B")

        # Insert cell rows with label and values
        data_ = [
            ("Ticket ID", self.id),
            ("Total", self.total),
            ("Seat ID", self.seat_id),
            ("Client name", self.client_name),
            ("Timestamp", self.timestamp)
        ]
        w_half = (pdf.w - pdf.r_margin - pdf.x) / 2

        for label, value_ in data_:
            pdf.set_font(family="Times", size=14, style="B")
            pdf.cell(w=w_half, h=40, txt=label, border=1)
            """
            `ln` Indicates where the current position should go after the call. Possible values are:
                0: to the right
                1: to the beginning of the next line
                2: below
            """
            pdf.set_font(family="Times", size=13)
            pdf.cell(w=w_half, h=40, txt=str(value_), border=1, ln=1)

        pdf.output(filepath)