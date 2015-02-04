from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='')
#Main DEW page
@app.route('/')
def home():
    return render_template("index.html")

#About page
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/us', methods=['GET'])
def us():
    return open('static/us.json').read()

@app.route('/data', methods=['GET'])
def data():
    return open('static/dewmvpv1.json').read()


if __name__ == '__main__':
    app.run(debug=True)
