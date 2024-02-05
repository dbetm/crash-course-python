from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flatmates_bill import Bill, Flatmate


app = Flask(__name__)


class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        form = BillForm()
        return render_template("bill_form_page.html", bill_form=form)


class ResultsPage(MethodView):
    def post(self):
        form = BillForm(request.form)

        amount = float(form.amount.data)
        period = form.period.data
        the_bill = Bill(amount, period)

        name1 = form.name1.data
        days_in_house1 = int(form.days_in_house1.data)
        flatmate1 = Flatmate(name1, days_in_house1)

        name2 = form.name2.data
        days_in_house2 = int(form.days_in_house2.data)
        flatmate2 = Flatmate(name2, days_in_house2)

        debt_flatmate1 = flatmate1.pay(the_bill, [flatmate2])
        debt_flatmate2 = flatmate2.pay(the_bill, [flatmate1])

        return render_template(
            "results_page.html",
            name1=name1,
            amount1=round(debt_flatmate1, 2),
            name2=name2,
            amount2=round(debt_flatmate2, 2),
        )


class BillForm(Form):
    amount = StringField(label="Bill amount: ", default="100")
    period = StringField(label="Bill period: ", default="February 2024")

    name1 = StringField(label="Name: ", default="Mary")
    days_in_house1 = StringField(label="Days in the house: ", default="20")

    name2 = StringField(label="Name: ", default="John")
    days_in_house2 = StringField(label="Days in the house: ", default="10")

    button = SubmitField(label="Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill_form", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))


app.run(debug=True)