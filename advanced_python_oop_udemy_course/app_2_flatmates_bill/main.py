import os

from flat import Bill, Flatmate
from reports import PDFReport, FileSharer


amount = float(input("Hey user, give me the bill amount: "))
period = input("Type the time period (example: January 2020): ")

bill = Bill(amount, period)

number_flatmates = 2
flatmates = []

for i in range(number_flatmates):
    name = input(f"What is your name? F - {i+1}: ")
    days_in_house = int(input(f"How many days did {name} stay in the house during the bill period? "))
    flatmate = Flatmate(name, days_in_house)

    flatmates.append(flatmate)

for flatmate in flatmates:
    co_flatmates = flatmate.get_co_flatmates(flatmates)
    print(f"{flatmate.name} pays: ", flatmate.pay(bill=bill, co_flatmates=co_flatmates))

basepath = os.path.dirname(os.path.abspath(__file__))
filename = f"bill_{bill.period}.pdf"

pdf_report = PDFReport(basepath=basepath, filename=filename)
pdf_report.generate(flatmates=flatmates, bill=bill)

# upload pdf to cloud
# filepath = f"{basepath}/files/reports/{filename}"
# filesharer = FileSharer(filepath=filepath, api_key="generate in filestack for free")