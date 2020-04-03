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
    else:
        x = "等一下"
        y = "等一下"
        z = "等一下"

    return render_template("view.html", form=form, x=x, y=y, z=z)

app.run(debug=True)
