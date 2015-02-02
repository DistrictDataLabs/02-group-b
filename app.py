from flask import Flask, render_template
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)
#Main DEW page
@app.route('/')
def home():
    return render_template("index.html")

#About page
@app.route('/about')
def about():
    return render_template("about.html")

#Sending the us.json file
@app.route('/usmap/')
def usmap():
    return "<a href=%s>file</a>" % url_for('static', filename='us.json')

#Sending our data
@app.route('/data/')
def data():
    return "<a href=%s>file</a>" % url_for('static', filename='dewmvp1.json')


if __name__ == '__main__':
    app.run(debug=True)
