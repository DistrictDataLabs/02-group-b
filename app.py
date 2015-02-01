from flask import Flask, render_template

app = Flask(__name__)
#Main DEW page
@app.route('/')
def home():
    return render_template("index.html")

#About page
@app.route('/about')
def about():
    return render_template("about.html")


static = Flask(__name__, static_url_path='/static')
assets = Flask(__name__, static_url_path='/assets')
data = Flask(__name__, static_url_path='/data')

if __name__ == '__main__':
    app.run(debug=True)
