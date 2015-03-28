from flask import Flask, render_template, redirect, request

app = Flask(__name__, static_folder='static', static_url_path='')
#Home
@app.route('/')
def home():
    return render_template("index.html")

#Platform
@app.route('/platform')
def platform():
    return render_template("platform.html")

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
