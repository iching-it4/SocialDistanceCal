#-*- coding: UTF-8 -*-

from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators

app = Flask(__name__)

# Model
class InputForm(Form):
    m = FloatField(validators=[validators.InputRequired()])
    n = FloatField(validators=[validators.InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        m = form.m.data
        n = form.n.data
        x = (m+1)//0.62
        y = n//1.84
        z = x*y
 
    return render_template("view.html", x=x, y=y, z=z)


if __name__ == '__main__': app.run(debug=True)
