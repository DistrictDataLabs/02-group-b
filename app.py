from flask import Flask, render_template, redirect, request
from flask_wtf import Form
from wtforms import TextField, SubmitField

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = 'development key'

class MyForm(Form):
    state = TextField("State")
    submit = SubmitField("Send")

#Home
@app.route('/')
def home():
    return render_template("index.html")

#Platform
@app.route('/platform', methods=['GET', 'POST'])
def platform():
    form = MyForm()
    return render_template("platform.html", form = form)

#Cluster view
@app.route('/cluster')
def cluster():
    return render_template("cluster.html")

#How to use
@app.route('/howto')
def howto():
    return render_template("howto.html")

#Methodology
@app.route('/methodology')
def methodology():
    return render_template("methodology.html")

#About page
@app.route('/about')
def about():
    return render_template("about.html")


#Advanced routing
@app.route('/local')
def local():
    return render_template("local.html")

#Data test page
@app.route('/data')
def data():
    return render_template("data.html")

if __name__ == '__main__':
    app.run(debug=True)
