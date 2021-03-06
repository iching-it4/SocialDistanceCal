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
        x = (m*100+150)//334
        y = (n*100+150)//212
        z = x*y
        a = (m*100+150)//225
        b = (m*100+150)//196
        c = a*b
        d = (m*100+150)//210
        e = (m*100+150)//196
        f = d*e
        
    else:
        x = "__"
        y = "__"
        z = "__"
        a = "__"
        b = "__"
        c = "__"
        d = "__"       
        e = "__"
        f = "__"  
    return render_template("OuOu.html", form=form, x=x, y=y, z=z,
                           a=a, b=b, c=c, d=d, e=e,f=f)


if __name__ == '__main__': app.run(debug=True)
