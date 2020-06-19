import sys
from flask import Flask, request, render_template, url_for, redirect, make_response, session


app = Flask(__name__)
app.secret_key = 'kpkhant007'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/second")
def home2():
    dict1 = {'hconame': 'Exact Science', 'provider': 'K Khant', 'npi': '1548862593', 'address': '81, Sarita Vihar', 'city': 'Surat', 'phone': '9016243435', 'fax': '459335'}
    return render_template("second.html", dict1 = dict1)


if __name__ == "__main__":
    app.run(debug=True)