from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
   
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
        return render_template("results.html", a= city, b = toDo)