import os
from typing import List
import webbrowser

from filestack import Client
from fpdf import FPDF


from flat import Bill, Flatmate


class PDFReport:

    def __init__(self, basepath: str, filename: str):
        self.basepath = basepath
        self.filename = filename

    def generate(self, flatmates: List[Flatmate], bill: Bill) -> None:
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image(f"{self.basepath}/files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Setup font
        pdf.set_font(family="Times", size=14, style="B")

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Setup font
        pdf.set_font(family="Times", size=12)

        # insert name and due amount for each flatmate
        for flatmate in flatmates:
            pdf.cell(w=100, h=40, txt=flatmate.name, border=1)
            co_flatmates = flatmate.get_co_flatmates(flatmates)
            due_amount = round(flatmate.pay(bill, co_flatmates=co_flatmates), 2)

            pdf.cell(w=150, h=40, txt=str(due_amount), border=1, ln=1)

        filepath = f"{self.basepath}/files/reports/{self.filename}"
        pdf.output(filepath)

        webbrowser.open("file://" + os.path.realpath(filepath))


class FileSharer:
    def __init__(self, filepath: str, api_key: str = "your api key"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self) -> str:
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)

        return new_filelink.url