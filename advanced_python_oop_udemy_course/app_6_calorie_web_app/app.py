from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField

from calorie import Calorie
from temperature import Temperature



app = Flask(__name__)
WEB_PAGES_TITLE = "Calories calculator"


class HomePage(MethodView):
    def get(self):
        return render_template("index.html", title=WEB_PAGES_TITLE)


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()

        return render_template(
            "calories_form_page.html", calories_form=calories_form, title=WEB_PAGES_TITLE
        )


    def post(self):
        calories_form = CaloriesForm(request.form)
        temperature = Temperature(
            country=calories_form.country.data,
            city=calories_form.city.data,
        ).get()

        calorie = Calorie(
            weight=int(calories_form.weight.data),
            height=int(calories_form.height.data),
            age=int(calories_form.age.data),
            temperature=temperature
        )

        calories = calorie.calculate()

        return render_template(
            "calories_form_page.html",
            calories_form=calories_form,
            calories=calories,
            title=WEB_PAGES_TITLE,
            result=True,
        )



class CaloriesForm(Form):
    """Class that contains the field definitions for the required data to compute the 
    calories a person needs.
    """
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=25)
    country = StringField("Country: ", default="Mexico")
    city = StringField("City: ", default="Veracruz")

    button = SubmitField(label="Calculate :)")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule(
    "/calories_form",
    view_func=CaloriesFormPage.as_view("calories_form_page")
)


app.run(debug=True)
