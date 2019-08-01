from app import app
from flask import render_template, request
from app.models import model, formopener
import random

@app.route('/')
@app.route('/index')
def index():
    randomCity = model.cities[random.randint(0, len(model.cities)-1)]
    randomCityUrl = model.SHOW_IMG(randomCity)
    return render_template("index.html", randomCityUrl = randomCityUrl)
   
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return render_template("results.html")
    else:
        print(request.form)
        userdata = dict(request.form)
        print(userdata)
        city = userdata["city"]
        toDo = model.my_destination(city)
        toEat = model.my_restaurants(city)
        currency = model.my_currency(city)
        img_url = model.SHOW_IMG(city)
        print(toDo)
        return render_template("results.html", a= city, b = toDo, c=img_url, d= toEat, e= currency)