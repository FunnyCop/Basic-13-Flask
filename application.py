from logging import debug
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/algorithm/', methods=['POST'])
def algorithm():
    select = request.form.get('algorithm')
    return render_template(select)

if __name__ == "__main__":
    app.run(debug=True)